from django import forms
from django.core.exceptions import ValidationError
from .models import Todo


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

