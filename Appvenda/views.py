from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from django.http import JsonResponse
from .models import *
from .form import *

# Create your views here.

def index(request):
    return render(request, 'exibidr.html')

def produtos(request):
    produtos = product.objects.all()

    context = {'produtos': produtos}
    return render(request, 'exibir.html', context)
    
def exibir_produtos(request):
    produtos = get_list_or_404(product)
    data = {'produtos': list(produtos.values())}
    return JsonResponse(data)

def create_produto(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    context = {
        'form': ProductForm
        }
    return render(request, 'create_produto.html', context)

    

def create_product_form(request):
    product = ClientForm(request.POST or None)
    if request.method == 'POST':
        
        
        if ClientForm.is_valid():
            
            product.save()
            return redirect('create_produto')
        

    return render(request, 'create_produto.html')