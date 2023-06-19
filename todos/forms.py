from django import forms
from django.core.exceptions import ValidationError
from .models import Todo, User


class TodoForm(forms.ModelForm):


    class Meta:
        model = Todo
        fields = ['name', 'description', 'user']


    def clean_name(self):
        if len(self.cleaned_data.get('name')) < 3:
            raise ValidationError('Name must be more than 2 characters')
        return self.cleaned_data.get('name')

    def clean_description(self):
        if len(self.cleaned_data.get('description')) > 100:
            raise ValidationError('Description must be less than 100')
        return self.cleaned_data.get('description')

class TodoUpdateForm(TodoForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    completed = forms.ChoiceField(choices = (("True",True), ("False", False)))
    description = forms.CharField(required=False)

    class Meta:
        model = Todo
        fields = ['name', 'description', 'user', 'completed']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['name'] = cleaned_data.get('name') or self.instance.name
        cleaned_data['description'] = cleaned_data.get('description') or self.instance.description
        cleaned_data['user'] = cleaned_data.get('user') or self.instance.user
        cleaned_data['completed'] = cleaned_data.get('completed') or self.instance.completed
