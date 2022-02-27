from tasks.models import Task
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        user = UserSerializer()
        model = Task
        fields = '__all__'

class TaskCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task.category
        fields = '__all__'
