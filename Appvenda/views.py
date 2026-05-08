from django.http import HttpResponse
from django.shortcuts import render
from .models import lista_produtos
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def produtos(request):
    context = lista_produtos[0].__dict__
    return render(request, 'exibir.html', context)
