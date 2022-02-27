from django.shortcuts import render
from django.http import HttpResponse
from budget.models import Budget
from budget.forms import add_budget_form, edit_budget_form
from core.models import UserProfile
#from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
#    return redirect("home")


def sum(request):
	obj=Budget.objects.all().aggregate(Sum('projected'))
	return render(request, 'budget/view_budget_list.html',{"obj": obj})


@login_required(login_url='/login/')
def budget(request):
	if not request.user.is_authenticated:
		return render(request, 'core/login.html')
	else:
		if request.method == 'POST':
			t_form = edit_budget_form(request.POST)
			if(t_form.is_valid()):

				budget_list_data = Budget.objects.get(id=t_form.cleaned_data["Ids"])
				budget_list_data.description = t_form.cleaned_data["Description"]
				budget_list_data.category = t_form.cleaned_data["Category"]
				budget_list_data.projected=t_form.cleaned_data["Projected"]
				budget_list_data.actual=t_form.cleaned_data["Actual"]
				budget_list_data.save()

	the_value_proj = Budget.objects.all().aggregate(Sum('projected'))
	the_value_actual = Budget.objects.all().aggregate(Sum('actual'))
	the_final_value = 0
	if the_final_value is not None:
		the_final_value = 0
		budget_obj = Budget.objects.select_related().filter(user=request.user)
		return render(request, 'budget/view_budget_list.html',{"allbudget": budget_obj, "the_final_value":the_final_value})
	else:
		the_final_value = the_value_proj['projected__sum'] - the_value_actual['actual__sum']
		budget_obj = Budget.objects.select_related().filter(user=request.user)
		return render(request, 'budget/view_budget_list.html',{"allbudget": budget_obj, "the_final_value":the_final_value})
	return render(request, 'budget/view_budget_list.html',{"allbudget": budget_obj, "the_final_value":the_final_value})

def add_budget(request):
	if (request.method == 'POST'):
		form = add_budget_form(request.POST)
		if (form.is_valid()):
			Description = form.cleaned_data['Description']  #names on the left are from form
			Category = form.cleaned_data['Category']           #bracket names are same as left
			Projected=form.cleaned_data['Projected']
			Actual=form.cleaned_data['Actual']
			Budget(user=request.user,description=Description, category=Category,projected=Projected,actual=Actual).save()   #first para on the left are from model
			budget_obj = Budget.objects.select_related().filter(user=request.user)
			return render(request,'budget/view_budget_list.html',{'allbudget':budget_obj})
	
	return render(request,'budget/add_budget.html',{"budgetform":add_budget_form})


def edit_budget(request):
		list=Budget.objects.get(id=request.GET['e_id'])
		data={}
		array={}
		array['Ids']=list.id
		array['Description']=list.description
		array['Category']=list.category
		array['Projected']=list.projected
		array['Actual']=list.actual
		forms=edit_budget_form(request.POST or None,initial=array)
		data['forms']=forms

		return render(request,'budget/edit_budget.html',data)


def delete_budget(request):
	ddata = Budget.objects.get(id=request.GET['delete'])
	ddata.delete()
	try:
		
		tasks_obj = Budget.objects.select_related().filter(user=request.user)
		return render(request, 'budget/view_budget_list.html', {"allbudget": tasks_obj})
	except Budget.DoesNotExist:
		tasks_obj = None
	return render(request, 'budget/view_Budget_list.html', {"allbudget": tasks_obj})


