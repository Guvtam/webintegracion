from django.urls import path
from carrito import views
from django.contrib.auth.decorators import login_required

app_name="carro"

urlpatterns=[
    path('carrito/',login_required(views.carritoCompra),name='carrito'),
    path('carrito/agregar/<int:producto_id>/',views.agregarProducto, name='agregar'),
    path('carrito/eliminar/<int:producto_id>/',views.eliminarProducto, name='eliminar'),
    path('carrito/restar/<int:producto_id>/',views.restarProducto, name='restar'),
    path('carrito/limpiar/',views.limpiarCarrito, name='limpiar'),
]