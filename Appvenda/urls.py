from .views import index
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('produtos/', produtos, name='produtos'),
    path('create_produto/', create_product, name='create_product'),
    path('display_products/', display_products, name='display_products'),
]