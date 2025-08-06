from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()   # 查询所有数据
    serializer_class = TodoItemSerializer   # 关联序列化器