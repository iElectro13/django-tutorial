from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='Home'),
    path('create-todo', views.create_todo, name='create-todo')
]