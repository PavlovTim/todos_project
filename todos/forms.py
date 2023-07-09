from django import forms
from django.core.exceptions import ValidationError
from .models import Todo, User, Priority, Label


class TodoForm(forms.ModelForm):
    description = forms.CharField(max_length=255, widget=forms.Textarea)
    priority = forms.ChoiceField(choices=Priority.priority_choise)

    class Meta:
        model = Todo
        fields = ['name', 'description', 'user', 'parent_todo', 'priority', 'label']

    def clean_name(self):
        if len(self.cleaned_data.get('name')) < 3:
            raise ValidationError('Name must be more than 2 characters')
        return self.cleaned_data.get('name')

    def clean_description(self):
        if len(self.cleaned_data.get('description')) > 255:
            raise ValidationError('Description must be less than 100')
        return self.cleaned_data.get('description')

    def clean_priority(self):
        return Priority.objects.get(value=self.cleaned_data['priority'])


class TodoUpdateForm(TodoForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    completed = forms.ChoiceField(choices=(("True",True), ("False", False)))
    description = forms.CharField(max_length=255, widget=forms.Textarea)

    class Meta:
        model = Todo
        fields = ['id', 'name', 'description', 'user', 'parent_todo',
                  'priority', 'label', 'completed']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['name'] = cleaned_data.get('name') or self.instance.name
        cleaned_data['description'] = cleaned_data.get('description') or self.instance.description
        cleaned_data['user'] = cleaned_data.get('user') or self.instance.user
        cleaned_data['priority'] = cleaned_data.get('priority') or self.instance.priority
        cleaned_data['parent_todo'] = cleaned_data.get('parent_todo') or self.instance.parent_todo
        cleaned_data['label'] = cleaned_data.get('label') or self.instance.label
        cleaned_data.get('completed') if cleaned_data.get('completed') is not None else self.instance.completed


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password_2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


