from django.urls import path

from . import views

urlpatterns = [
    path('/', views.json_out),
    path('/home', views.home),
    path('/<int:id>', views.get_todo),
    path('/create', views.create_todo)
]