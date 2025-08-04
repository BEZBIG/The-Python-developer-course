from django.shortcuts import render

# Класс HttpResponse нужно импортировать в код из модуля django.http.
from django.http import HttpResponse

def index(request):    
    return HttpResponse('Главная страница')
