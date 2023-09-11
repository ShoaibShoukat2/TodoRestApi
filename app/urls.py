from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view(),name="list of todo"),
    path('create', CreateTodo.as_view(),name="create todo"),
    path('delete/<int:pk>', DeleteTodo.as_view())
]
