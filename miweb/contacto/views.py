
from contacto.forms import FormularioContacto


from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import FormularioContacto

def contacto(request):
    form = FormularioContacto()
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            contenido = form.cleaned_data['contenido']

            mail = EmailMessage(
                subject="Mensaje desde la app Django",
                body="El usuario {} con el correo {} escribe:\n\n{}".format(nombre, email, contenido),
                from_email="gutierrez.valdes.t@gmail.com",
                to=["gutierrez.valdes.t@gmail.com"],
                reply_to=[email]
            )

            try:
                mail.send()
                return redirect('/contacto/?valido')
            except Exception as e:
                print(str(e))  # Imprime el error en la consola para depuración
                return redirect('/contacto/?novalido')

    return render(request, 'contacto/contacto.html', {'form': form})
