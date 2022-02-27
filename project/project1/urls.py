"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from tasks import views as tasks_views
from budget import views as budget_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),

    path('tasks/', tasks_views.tasks, name='tasks'),
    path('tasks/add/', tasks_views.add, name='tasks_add'),
    path('tasks/edit/', tasks_views.edit, name='tasks_edit'),

    path('budget/', budget_views.budget, name='budget'),
    path('add_budget/', budget_views.add_budget, name='add_budget'),
    path('edit_budget/', budget_views.edit_budget, name='edit_budget'),
    path('delete_budget/', budget_views.delete_budget, name='delete_budget'),

    path('about/', core_views.about, name='about'),
    path('machu.jpg', core_views.about, name='picofu'),

    path('login/', core_views.login, name='login'),
    path('logout/', core_views.logout, name='logout'),
    path('join/', core_views.join, name='join')
]
