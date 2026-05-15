from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from django.http import JsonResponse
from .models import *
from .form import *

# Create your views here.

def index(request):
    return render(request, 'exibidr.html')

def produtos(request):
    produtos = Product.objects.all()

    context = {'produtos': produtos}
    return render(request, 'exibir.html', context)
    
def exibir_produtos(request):
    produtos = get_list_or_404(Product)
    data = {'produtos': list(produtos.values())}
    return JsonResponse(data)
   

def display_products(request):
    
    product = get_list_or_404(Product.objects.all())
    context = {'product': product}
    return render(request, 'exibir.html', context)

def create_product(request):
    
    product = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        
        if product.is_valid():
            
            product.save()

            return redirect('create_product')
        
    form = ProductForm()    
    context = {
        "form": form
        }   
    
    return render(request, 'create_produto.html', context)