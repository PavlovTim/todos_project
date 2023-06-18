from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_json),
    path('home', views.home, name='home'),
    path('<int:id>', views.get_todo),
    path('create', views.create_todo),
]