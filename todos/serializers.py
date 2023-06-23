from todos.models import Todo
from django.contrib.auth.models import User
from rest_framework import serializers


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Todo
        fields = ['id', 'name', 'description', 'user', 'completed']