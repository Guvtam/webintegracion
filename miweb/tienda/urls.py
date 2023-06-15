from django.urls import path
from tienda import views

urlpatterns=[
    path('tienda/',views.tienda,name='tienda'),
    path('tienda/categorias/<int:categoria_id>/',views.categorias,name='categorias'),
]