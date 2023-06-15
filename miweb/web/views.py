from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'web/home.html')




def contacto(request):
    return render(request,'web/contacto.html')





