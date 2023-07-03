from todos.models import Todo, Priority, Label
from django.contrib.auth.models import User
from rest_framework import serializers


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    priority = serializers.SlugRelatedField(slug_field="value", queryset=Priority.objects.all())
    label = serializers.SlugRelatedField(slug_field="name", queryset=Label.objects.all())

    class Meta:
        model = Todo
        fields = ['id', 'name', 'description', 'user', 'parent_todo', 'priority', 'label', 'completed']