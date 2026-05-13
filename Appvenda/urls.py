from .views import index
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('produtos/', produtos, name='produtos'),
    path('create_produto/', create_produto, name='create_produto'),
]