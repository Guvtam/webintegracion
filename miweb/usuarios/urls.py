
from django.urls import path
from .views import VRegistro, iniciarSesion, cerrarSesion

urlpatterns=[
    path('autenticacion/',VRegistro.as_view(),name='autenticacion'),
    path('login/',iniciarSesion,name='iniciarSesion'),
    path('logout/',cerrarSesion,name='cerrarSesion'),
    
]