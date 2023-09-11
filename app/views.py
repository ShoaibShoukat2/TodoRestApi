from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

# Create your views here.



class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
