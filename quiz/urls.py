from django.urls import path, re_path
from .views import (
    QuizListView, CategoriesListView, ViewQuizListByCategory, 
    QuizUserProgressView, QuizMarkingList, QuizMarkingDetail, 
    QuizDetailView, QuizTake, index, login_user, logout_user, 
    mark_as_read, TabsitModuleView, TaqidModuleView
)

urlpatterns = [
    path('index/', index, name='index'),
    path('tabsit/module<int:module_number>/', TabsitModuleView.as_view(), name='tabsit_module'),
    path('taqid/module<int:module_number>/', TaqidModuleView.as_view(), name='taqid_module'),
    path('mark_as_read/<int:message_id>/', mark_as_read, name='mark_as_read'),
    
    # Login/Logout URLs
    path('', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    
    # Quiz URLs
    path('quizzes/', QuizListView.as_view(), name='quiz_index'),
    path('category/', CategoriesListView.as_view(), name='quiz_category_list_all'),
    re_path(r'^category/(?P<category_name>[\w|\W-]+)/$', ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),
    path('progress/', QuizUserProgressView.as_view(), name='quiz_progress'),
    path('marking/', QuizMarkingList.as_view(), name='quiz_marking'),
    re_path(r'^marking/(?P<pk>[\d.]+)/$', QuizMarkingDetail.as_view(), name='quiz_marking_detail'),
    
    # Dynamic URLs based on slug and quiz_name
    re_path(r'^(?P<slug>[\w-]+)/$', QuizDetailView.as_view(), name='quiz_start_page'),
    re_path(r'^(?P<quiz_name>[\w-]+)/take/$', QuizTake.as_view(), name='quiz_question'),
]
