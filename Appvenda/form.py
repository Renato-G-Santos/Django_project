from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'value', 'description', 'category', 'lot', 'image', 'stock']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name', }),
        'value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Product Value', 'step': '0.01'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Product Description'}),
        'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select a category'}),
        'lot': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Lot'}),
        'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Product Stock'}),
    }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
    }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'cpf']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Client Email'}),
        'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Phone'}),
        'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client CPF'}),
    }