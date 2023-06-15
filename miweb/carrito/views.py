from django.shortcuts import render, redirect
from carrito.carro import Carrito
from tienda.models import Producto
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def carritoCompra(request):
    return render(request,'carrito/carro.html')

def agregarProducto(request,producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect('tienda')

def eliminarProducto(request,producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect('carro:carrito')

def restarProducto(request,producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.restar_producto(producto=producto)
    return redirect('carro:carrito')

def limpiarCarrito(request,producto_id):
    carrito=Carrito(request)
    carrito.limpiar_carrito()
    return redirect('carro:carrito')

