from cgi import print_arguments
from django.db import models

# Create your models here.

class Categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

class Comida(models.Model):
    marca = models.CharField(max_length=20, primary_key=True, verbose_name='Marca')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    tamanno = models.CharField(max_length=4, verbose_name='Tamaño')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.marca

class User(models.Model):
    idUser = models.IntegerField(primary_key=True, verbose_name='Id de usuario')
    nombreUser = models.CharField(max_length=50, verbose_name='Nombre del usuario')
    
    def __str__(self):
        return self.nombreUser

class Cliente(models.Model):
    rut = models.IntegerField(primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut
