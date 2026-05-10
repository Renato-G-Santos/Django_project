from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from .models import produto

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def produtos(request):
    produtos = produto.objects.all()
    produtos = get_list_or_404(produto)
    context = {'produtos': produtos}
    return render(request, 'exibir.html', context)
    
