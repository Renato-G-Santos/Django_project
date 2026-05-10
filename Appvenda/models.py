from django.db import models

# Create your models here.

class categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, default=1)
    lote = models.CharField(max_length=100, default= 1)
    def __str__(self):
        return self.nome
    
