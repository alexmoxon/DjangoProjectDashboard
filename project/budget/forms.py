from django import forms
from django.core import validators
from .models import Budget

CATEGORIES= [
    ('food','Food'),
    ('clothing', 'Clothing'),
    ('housing','Housing'),
    ('education','Education'),
	('entertainment','Entertainment'),
    ('other','Other'),
    ]

class add_budget_form(forms.Form):
	Description= forms.CharField(max_length=100, label='Description')
	Category= forms.CharField(label='Category', widget=forms.Select(choices=CATEGORIES))
	Projected=forms.IntegerField(initial=0)
	Actual=forms.IntegerField(initial=0)

class edit_budget_form(forms.Form):
	Ids=forms.CharField(widget=forms.HiddenInput())
	Projected=forms.IntegerField(initial=0)
	Actual=forms.IntegerField(initial=0)
	Description=forms.CharField(max_length=100, label='Description')
	Category=forms.CharField(label='Category', widget=forms.Select(choices=CATEGORIES))
