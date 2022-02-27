from django import forms
from django.core import validators
from tasks.models import Task
from core.models import UserProfile

CATEGORIES= [
    ('home','Home'),
    ('school', 'School'),
    ('work','Work'),
    ('self-employement','Self-employement'),
    ('other','Other'),
    ]

STATUS= [
	('Yes','Yes'),
	('No','No')
]

class add_task_form(forms.Form):
	Description= forms.CharField(max_length=100, label='Description')
	Category= forms.CharField(label='Category', widget=forms.Select(choices=CATEGORIES))

class edit_task_form(forms.Form):
	Ids=forms.CharField(widget=forms.HiddenInput())
	is_completed=forms.ChoiceField(choices=STATUS)
	Description=forms.CharField(max_length=100, label='Description')
	Category=forms.CharField(label='Category', widget=forms.Select(choices=CATEGORIES))

class HideCompletedTasksForm(forms.ModelForm):
    tasks_view_hide_completed = forms.BooleanField(required = False, label='Hide Completed Tasks', widget=forms.CheckboxInput(attrs={'onclick': 'this.form.submit()'}))
    class Meta():
        model = UserProfile
        fields = ['tasks_view_hide_completed',]
        labels = {
            "tasks_view_hide_completed": "Hide Completed Tasks"
        }
