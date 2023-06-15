from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created =models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ='categoriaProducto'
        verbose_name_plural='categoriasProducto'

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca =models.CharField(max_length=50)
    descripcion =models.CharField(max_length=50)
    imagen =models.ImageField(upload_to='productos/')
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    precio=models.IntegerField(blank=False,default=0)
    disponible=models.BooleanField(default=True)
    stock=models.IntegerField(blank=False,default=0)
    created =models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name ='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre

