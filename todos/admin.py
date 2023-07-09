from django.contrib import admin

from todos.models import Todo, Label, Priority

admin.site.register(Todo)
admin.site.register(Label)
admin.site.register(Priority)