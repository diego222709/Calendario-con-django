from django.shortcuts import render, redirect
from .models import Actividad

def home(request):
    return render(request, "principal.html")

def fecha(request):
    actividades = Actividad.objects.all()
    print(actividades)  # Check the data in the console
    return render(request, 'fecha.html', {'actividades': actividades})


from .models import Actividad

def calendario(request):
    actividades = Actividad.objects.all()  # Recupera todas las actividades de la base de datos
    return render(request, 'calendaio.html', {'actividades': actividades})


def registrar_fechas(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        fecha_hora_inicio = request.POST['fechainicio']
        fecha_hora_salida = request.POST['fechafin']

        actividad = Actividad(
            codigo=codigo,
            nombre=nombre,
            fecha_hora_inicio=fecha_hora_inicio,
            fecha_hora_salida=fecha_hora_salida
        )
        actividad.save()
        return redirect('fecha')  # Redirect to the 'fecha' page or any other page you prefer
    
# Create your views here.
