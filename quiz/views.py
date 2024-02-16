import random

from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import FormView
from .forms import QuestionForm,GPTForm
from .models import Quiz, Category, Progress, Sitting, Question
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages













class QuizMarkerMixin(object):
    @method_decorator(login_required)
    @method_decorator(permission_required('quiz.view_sittings'))
    def dispatch(self, *args, **kwargs):
        return super(QuizMarkerMixin, self).dispatch(*args, **kwargs)


class SittingFilterTitleMixin(object):
    def get_queryset(self):
        queryset = super(SittingFilterTitleMixin, self).get_queryset()
        quiz_filter = self.request.GET.get('quiz_filter')
        if quiz_filter:
            queryset = queryset.filter(quiz__title__icontains=quiz_filter)

        return queryset


class QuizListView(ListView):
    model = Quiz
    # @login_required
    def get_queryset(self):
        queryset = super(QuizListView, self).get_queryset()
        print(queryset)
        return queryset.filter(draft=False)


class QuizDetailView(DetailView):
    model = Quiz
    slug_field = 'url'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.draft and not request.user.has_perm('quiz.change_quiz'):
            raise PermissionDenied

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class CategoriesListView(ListView):
    model = Category


class ViewQuizListByCategory(ListView):
    model = Quiz
    template_name = 'view_quiz_category.html'

    def dispatch(self, request, *args, **kwargs):
        self.category = get_object_or_404(
            Category,
            category=self.kwargs['category_name']
        )

        return super(ViewQuizListByCategory, self).\
            dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewQuizListByCategory, self)\
            .get_context_data(**kwargs)

        context['category'] = self.category
        return context

    def get_queryset(self):
        queryset = super(ViewQuizListByCategory, self).get_queryset()
        return queryset.filter(category=self.category, draft=False)


class QuizUserProgressView(TemplateView):
    template_name = 'progress.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(QuizUserProgressView, self)\
            .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuizUserProgressView, self).get_context_data(**kwargs)
        progress, c = Progress.objects.get_or_create(user=self.request.user)
        context['cat_scores'] = progress.list_all_cat_scores
        context['exams'] = progress.show_exams()
        return context


class QuizMarkingList(QuizMarkerMixin, SittingFilterTitleMixin, ListView):
    model = Sitting

    def get_queryset(self):
        queryset = super(QuizMarkingList, self).get_queryset()\
                                               .filter(complete=True)

        user_filter = self.request.GET.get('user_filter')
        if user_filter:
            queryset = queryset.filter(user__username__icontains=user_filter)

        return queryset
    
    class Meta:
        pass


class QuizMarkingDetail(QuizMarkerMixin, DetailView):
    model = Sitting

    def post(self, request, *args, **kwargs):
        sitting = self.get_object()

        q_to_toggle = request.POST.get('qid', None)
        if q_to_toggle:
            q = Question.objects.get_subclass(id=int(q_to_toggle))
            if int(q_to_toggle) in sitting.get_incorrect_questions:
                sitting.remove_incorrect_question(q)
            else:
                sitting.add_incorrect_question(q)

        return self.get(request)

    def get_context_data(self, **kwargs):
        context = super(QuizMarkingDetail, self).get_context_data(**kwargs)
        context['questions'] =\
            context['sitting'].get_questions(with_answers=True)
        return context


class QuizTake(FormView):
    form_class = QuestionForm
    template_name = 'question.html'

    def dispatch(self, request, *args, **kwargs):
        self.quiz = get_object_or_404(Quiz, url=self.kwargs['quiz_name'])
        if self.quiz.draft and not request.user.has_perm('quiz.change_quiz'):
            raise PermissionDenied

        self.logged_in_user = self.request.user.is_authenticated

        if self.logged_in_user:
            self.sitting = Sitting.objects.user_sitting(request.user,
                                                        self.quiz)
        if self.sitting is False:
            return render(request, 'single_complete.html')

        return super(QuizTake, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class=QuestionForm):
        if self.logged_in_user:
            self.question = self.sitting.get_first_question()
            self.progress = self.sitting.progress()
        return form_class(**self.get_form_kwargs())

    def get_form_kwargs(self):
        kwargs = super(QuizTake, self).get_form_kwargs()

        return dict(kwargs, question=self.question)

    def form_valid(self, form):
        if self.logged_in_user:
            self.form_valid_user(form)
            if self.sitting.get_first_question() is False:
                return self.final_result_user()
        self.request.POST = {}

        return super(QuizTake, self).get(self, self.request)

    def get_context_data(self, **kwargs):
        context = super(QuizTake, self).get_context_data(**kwargs)
        context['question'] = self.question
        context['quiz'] = self.quiz
        if hasattr(self, 'previous'):
            context['previous'] = self.previous
        if hasattr(self, 'progress'):
            context['progress'] = self.progress
        return context

    def form_valid_user(self, form):
        progress, c = Progress.objects.get_or_create(user=self.request.user)
        guess = form.cleaned_data['answers']
        is_correct = self.question.check_if_correct(guess)

        if is_correct is True:
            self.sitting.add_to_score(1)
            progress.update_score(self.question, 1, 1)
        else:
            self.sitting.add_incorrect_question(self.question)
            progress.update_score(self.question, 0, 1)

        if self.quiz.answers_at_end is not True:
            self.previous = {'previous_answer': guess,
                             'previous_outcome': is_correct,
                             'previous_question': self.question,
                             'answers': self.question.get_answers(),
                             'question_type': {self.question
                                               .__class__.__name__: True}}
        else:
            self.previous = {}

        self.sitting.add_user_answer(self.question, guess)
        self.sitting.remove_first_question()

    def final_result_user(self):
        results = {
            'quiz': self.quiz,
            'score': self.sitting.get_current_score,
            'max_score': self.sitting.get_max_score,
            'percent': self.sitting.get_percent_correct,
            'sitting': self.sitting,
            'previous': self.previous,
        }

        self.sitting.mark_quiz_complete()

        if self.quiz.answers_at_end:
            results['questions'] =\
                self.sitting.get_questions(with_answers=True)
            results['incorrect_questions'] =\
                self.sitting.get_incorrect_questions

        if self.quiz.exam_paper is False:
            self.sitting.delete()
        print(results['quiz'].category.id)    
        if 'quiz' in results and results['quiz'].title == 'إختبار المقياس':
            # ========= taqid
            if results['score'] >= 8:
                messages.success(self.request, ' تم تجاوز المقياس  بنجاح درجتك = '+ str(results['score']))
                return render(self.request, 'measure_test/taeqid.html', results)
            # ========= tabsit
            elif results['score'] < 8:
                messages.success(self.request, 'لم يتم تجاوز المقياس درجتك = '+ str(results['score']))
                return render(self.request, 'measure_test/tabsit.html', results)
            #  =================== Qably 4aml all of this for taqid content
        if 'quiz' in results and results['quiz'].title == 'قبلي الشامل' and results['quiz'].category.id == 2 :
            if results['percent'] <= 90:
                messages.success(self.request, ' تم تجاوز المقياس  بنجاح درجتك = '+ str(results['score']))
                return render(self.request, 'taqid/module1.html', results)
            elif results['percent'] > 90:
                messages.success(self.request, 'لم يتم تجاوز المقياس درجتك = '+ str(results['score']))
                return render(self.request, 'taqid/2.html', results)
         # -------------------module 1   
        if 'quiz' in results and results['quiz'].title == 'الاختبار القبلى للموديول الاول':
            messages.success(self.request, ' تم تجاوز المقياس بنسبة  '+ str(results['percent']))
            return render(self.request, 'taqid/mo7ta_mod1.html', results)
        
        if 'quiz' in results and results['quiz'].title == 'الاختبار البعدى للموديول الاول' and results['quiz'].category.id == 2  :
            if results['percent'] >= 60:
                messages.success(self.request, ' تم تجاوز المقياس  بنسبة = '+ str(results['percent']))
                return render(self.request, 'taqid/module2.html', results)
            elif results['percent'] < 60:
                messages.success(self.request, 'لم يتم تجاوز بنسبة = '+ str(results['percent']))
                return render(self.request, 'taqid/mo7ta_mod1.html', results)
        #  ======================== module2
        if 'quiz' in results and results['quiz'].title == 'الاختبار القبلي للموديول الثانى' and results['quiz'].category.id == 2 :
            messages.success(self.request, ' تم تجاوز المقياس بنسبة  '+ str(results['percent']))
            return render(self.request, 'taqid/mo7ta_mod2.html', results)
        if 'quiz' in results and results['quiz'].title == 'الاختبار البعدى للموديول الثانى' and results['quiz'].category.id == 2 :
            if results['percent'] >= 60:
                messages.success(self.request, ' تم تجاوز المقياس  بنسبة = '+ str(results['percent']))
                return render(self.request, 'taqid/module3.html', results)
            elif results['percent'] < 60:
                messages.success(self.request, 'لم يتم تجاوز بنسبة = '+ str(results['percent']))
                return render(self.request, 'taqid/mo7ta_mod1.html', results)
        #  ======================== module3
        if 'quiz' in results and results['quiz'].title == 'الاختبار القبلي للموديول الثالث'and results['quiz'].category.id == 2 :
            messages.success(self.request, ' تم تجاوز المقياس بنسبة  '+ str(results['percent']))
            return render(self.request, 'taqid/mo7ta_mod3.html', results)
        if 'quiz' in results and results['quiz'].title == 'الاختبار البعدى للموديول الثانى' and results['quiz'].category.id == 2 :
            if results['percent'] >= 60:
                messages.success(self.request, ' تم تجاوز المقياس  بنسبة = '+ str(results['percent']))
                return render(self.request, 'taqid/module3.html', results)
            elif results['percent'] < 60:
                messages.success(self.request, 'لم يتم تجاوز بنسبة = '+ str(results['percent']))
                return render(self.request, 'taqid/mo7ta_mod3.html', results)
        
        #  =============   ====== Qably 4aml all of this for tabsit content
        if 'quiz' in results and results['quiz'].title == 'قبلي الشامل' and results['quiz'].category.id == 3 :
            if results['percent'] <= 90:
                messages.success(self.request, ' تم تجاوز المقياس  بنجاح درجتك = '+ str(results['score']))
                return render(self.request, 'tabsit/module1.html', results)
            elif results['percent'] > 90:
                messages.success(self.request, 'لم يتم تجاوز المقياس درجتك = '+ str(results['score']))
                return render(self.request, 'tabsit/2.html', results)
         # -------------------module 1   
        if 'quiz' in results and results['quiz'].title == 'الاختبار القبلى للموديول الاول'and results['quiz'].category.id == 3:
            messages.success(self.request, ' تم تجاوز المقياس بنسبة  '+ str(results['percent']))
            return render(self.request, 'tabsit/mo7ta_mod1.html', results)
        
        if 'quiz' in results and results['quiz'].title == 'الاختبار البعدى للموديول الاول'and results['quiz'].category.id == 3:
            if results['percent'] >= 60:
                messages.success(self.request, ' تم تجاوز المقياس  بنسبة = '+ str(results['percent']))
                return render(self.request, 'tabsit/module2.html', results)
            elif results['percent'] < 60:
                messages.success(self.request, 'لم يتم تجاوز بنسبة = '+ str(results['percent']))
                return render(self.request, 'tabsit/mo7ta_mod1.html', results)
        #  ======================== module2
        if 'quiz' in results and results['quiz'].title == 'الاختبار القبلي للموديول الثانى'and results['quiz'].category.id == 3:
            messages.success(self.request, ' تم تجاوز المقياس بنسبة  '+ str(results['percent']))
            return render(self.request, 'tabsit/mo7ta_mod2.html', results)
        if 'quiz' in results and results['quiz'].title == 'الاختبار البعدى للموديول الثانى'and results['quiz'].category.id == 3:
            if results['percent'] >= 60:
                messages.success(self.request, ' تم تجاوز المقياس  بنسبة = '+ str(results['percent']))
                return render(self.request, 'tabsit/module3.html', results)
            elif results['percent'] < 60:
                messages.success(self.request, 'لم يتم تجاوز بنسبة = '+ str(results['percent']))
                return render(self.request, 'tabsit/mo7ta_mod1.html', results)
        #  ======================== module3
        if 'quiz' in results and results['quiz'].title == 'الاختبار القبلي للموديول الثالث'and results['quiz'].category.id == 3:
            messages.success(self.request, ' تم تجاوز المقياس بنسبة  '+ str(results['percent']))
            return render(self.request, 'tabsit/mo7ta_mod3.html', results)
        if 'quiz' in results and results['quiz'].title == 'الاختبار البعدى للموديول الثانى'and results['quiz'].category.id == 3:
            if results['percent'] >= 60:
                messages.success(self.request, ' تم تجاوز المقياس  بنسبة = '+ str(results['percent']))
                return render(self.request, 'tabsit/module3.html', results)
            elif results['percent'] < 60:
                messages.success(self.request, 'لم يتم تجاوز بنسبة = '+ str(results['percent']))
                return render(self.request, 'tabsit/mo7ta_mod3.html', results)

        
        return render(self.request, 'result.html', results)



import openai
from django.http import JsonResponse

openai.api_key = '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'
def index(request):
    if request.method == 'POST':
        # Get user input
        user_input = request.POST['user_input']

        # Call the ChatGPT API to get a response
        response = openai.Completion.create(
            engine='gpt-3.5-turbo-instruct',
            prompt=f"Conversation with a user:\nUser: {user_input}\nAI:",
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the response text from the API result
        bot_response = response.choices[0].text.strip()

        # Return the response as JSON
        return JsonResponse({'bot_response': bot_response})
    return render(request, 'index.html', {})


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'مرحباً بــــــــــك : '+ username)
            return redirect("index")
        else:
            messages.success(request, 'خطأ بإسم المستخدم أو كلمة المرور ')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'تم تسجيل الخروج بنجاح ..')
    return redirect('login')

