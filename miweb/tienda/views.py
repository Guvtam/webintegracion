from django.shortcuts import render
from tienda.models import Categoria, Producto

# Create your views here.
def tienda(request):
    cat=Categoria.objects.all()
    prod=Producto.objects.all()
    return render(request,'tienda/tienda.html',{'cat': cat,'prod':prod})

def categorias(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    prod=Producto.objects.filter(categoria=categoria)
    cat=Categoria.objects.all()
    return render(request,'tienda/categorias.html',{'categoria': categoria,'prod':prod,'cat':cat})
