from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from main.models import UserInfo
from rest_framework.renderers import TemplateHTMLRenderer
from main.serializer import CreateUserSerializer, UserSerializer
from django.shortcuts import render
from django.http import HttpResponse


def menu(request):
    template_name = 'main/menu.html'
    pages = {
        'Создание нового пользователя': 'create/',
        'Просмотр информации пользователей': 'users/',
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def Users(request):
    template_name = 'main/list.html'
    pages = {
        'Просмотр конкретного пользователя': 'users/<pk>/',
        'Просмотр всех пользователей': 'users/list/',
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

 #создание пользователя
class CreateUser(ListCreateAPIView):     
    queryset = UserInfo.objects.all()
    serializer_class = CreateUserSerializer

#вывод данных по всем пользователям
class UsersList(ListAPIView):                  
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer

#вывод данных по одному пользователям
class OneUser(RetrieveAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer



