from django.urls import path

from . import views

urlpatterns = [
    path('/', views.json_out),
    path('/home', views.home, name='home'),
    path('/<int:id>', views.get_todo),
    path('/create', views.create_todo),
    path('/todo_db', views.todo_db)
]