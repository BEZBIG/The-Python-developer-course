from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def product_category(request, category):    
    return HttpResponse(f'Категория {category}') 