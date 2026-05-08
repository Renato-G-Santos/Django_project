from django.http import HttpResponse
from django.shortcuts import render
from .models import lista_produtos
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def produtos(request):
    context = lista_produtos[0]
    return HttpResponse(f"""
                        <h1>{context.nome}</h1>
                        <p>Preço: R${context.preco}</p>
                        <p>Descrição: {context.descricao}</p>
                        """)
