from django.db import models


# Create your models here.
class produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    def __str__(self):
        return self.nome
    

produto1 = produto(nome="Produto 1", preco=10.99, descricao="Descrição do Produto 1")
produto2 = produto(nome="Produto 2", preco=19.99, descricao="Descrição do Produto 2")
lista_produtos = [produto1, produto2]