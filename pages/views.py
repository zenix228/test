from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request, 'base.html')

def clothes(request):
    products = product1.objects.all()
    context = {
        'products': products
    }
    return render(request, 'pages/clothes.html', context) 

def clothes_detail(request, pk):
    products = product1.objects.get(id=pk)
    context = {
        'products': products
    }
    return render(request, 'pages/clothes_detail.html', context) 

def accesorries(request):
    products = product2.objects.all()
    context = {
        'products': products
    }
    return render(request, 'pages/accessories.html', context) 

def mobiles(request):
    products = product2.objects.all()
    context = {
        'products': products
    }
    return render(request, 'pages/mobile.html',context)

def electronics(request):
    products = product2.objects.all()
    context = {
        'products': products
    }
    return render(request, 'pages/electro.html',context)   