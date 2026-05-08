from .views import index
from django.urls import path
from .views import produtos

urlpatterns = [
    path('', index, name='index'),
    path('produtos/', produtos, name='produtos'),
]