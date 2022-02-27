from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from tasks.forms import add_task_form, edit_task_form, HideCompletedTasksForm
from core.models import UserProfile
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from tasks.serializers import TaskSerializer, TaskCategorySerializer, UserSerializer

# Create your views here.
@login_required(login_url='/login/')
def tasks(request):
    # Create some default categories if there aren't any.

    if (request.method == "GET" and "toggle_completed" in request.GET):
        id = request.GET["toggle_completed"]
        task = Task.objects.get(id=id)
        task.is_completed = not task.is_completed
        task.save()

    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        Task.objects.filter(id=id).delete()
        return redirect("/tasks/")

    if (request.method == "POST"):
        try:
            user_profile = UserProfile.objects.filter(user=request.user).get()
        except:
            user_profile = UserProfile();
            user_profile.user = request.user;
            user_profile.tasks_view_hide_completed = False

        form = HideCompletedTasksForm(request.POST, instance=user_profile)

        if (form.is_valid()):
            form.save()
    try:
        user_profile = UserProfile.objects.filter(user=request.user).get()
        hide_completed_form_data = HideCompletedTasksForm(instance=user_profile)
    except:
        hide_completed_form_data = HideCompletedTasksForm()

    hide_completed = hide_completed_form_data["tasks_view_hide_completed"].value()
    if (hide_completed):
        table_data = Task.objects.select_related().filter(user=request.user, is_completed=False)
    else:
        table_data = Task.objects.select_related().filter(user=request.user)
    context = {
        "hide_completed_form_data": hide_completed_form_data,
        "table_data": table_data
    }
    return render(request, 'tasks/tasks.html', context)

def add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            new_task_form = add_task_form(request.POST)
            if (new_task_form.is_valid()):
                description = new_task_form.cleaned_data["Description"]
                category = new_task_form.cleaned_data["Category"]
                user = User.objects.get(id=request.user.id)
                Task(user = user, description=description, category=category, is_completed=False).save()
                return redirect("/tasks/")
            else:
                context = {
                    "form_data": new_task_form
                }
                return render(request, 'tasks/add.html', context)
        else:
            # Cancel
            return redirect("/tasks/")

    else:
        context = {
            "form_data": add_task_form()
        }
        return render(request, 'tasks/add.html', context)

def edit(request):
		list=Task.objects.get(id=request.GET['e_id'])
		data={}
		array={}
		array['Ids']=list.id
		array['Description']=list.description
		array['Category']=list.category
		array['Completed']=list.is_completed

		forms=edit_task_form(request.POST or None,initial=array)
		data['forms']=forms

		return render(request,'tasks/edit.html',data)

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tasks to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Task Categories to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
