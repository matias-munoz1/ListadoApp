from django.shortcuts import render, get_object_or_404, redirect
from .models import Inscripcion
from .forms import InscripcionForm

def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'inscripciones/listar.html', {'inscripciones': inscripciones})

def agregar_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        print("Datos recibidos:", request.POST)  
        if form.is_valid():
            print("Formulario válido. Guardando...")
            form.save()
            return redirect('listar_inscripciones')
        else:
            print("Errores en el formulario:")
            print(form.errors)  
    else:
        form = InscripcionForm()
    return render(request, 'inscripciones/agregar.html', {'form': form})

def modificar_inscripcion(request, id):
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'inscripciones/modificar.html', {'form': form})

def eliminar_inscripcion(request, id):
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('listar_inscripciones')
    return render(request, 'inscripciones/eliminar.html', {'inscripcion': inscripcion})
