from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='todo-landing-page'),
    path('home/',views.home, name= 'todo-home'),
    path('todo/', views.todo, name='todo-list'),
    path('positivity/', views.positivity, name='todo-positivity'),
    path('goalform/',views.goalform,name='todo-goalform'),
    path('todoform/',views.todoform,name='todo-todoform'),
    

]

