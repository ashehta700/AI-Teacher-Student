# Generated by Django 2.2.7 on 2024-04-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0002_auto_20180727_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcqquestion',
            name='answer_order',
            field=models.CharField(blank=True, choices=[('content', 'Content'), ('none', 'None')], default='none', help_text='The order in which multichoice                     answer options are displayed                     to the user', max_length=30, null=True, verbose_name='Answer Order'),
        ),
    ]
