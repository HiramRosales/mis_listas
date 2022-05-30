from readline import append_history_file
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from mascotas.forms import MascotaForm, BuscarMascotasForm, ActualizarMascotaForm

from mascotas.models import Mascota

def index_mascotas(request):
    mascotas = Mascota.objects.all()
    template = loader.get_template('mascotas/lista_mascotas.html')
    context = {
        'mascotas': mascotas,
    }
    return HttpResponse(template.render(context, request))


def agregar_mascotas(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            tipo = form.cleaned_data['nombre']
            edad = form.cleaned_data['edad']
            peso = form.cleaned_data['peso']
            Mascota(nombre=nombre, tipo=tipo, edad=edad, peso=peso).save()

            return HttpResponseRedirect(reverse("index_mascotas"))
    elif request.method == "GET":
        form = MascotaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'mascotas/form_mascotas_carga.html', {'form': form})


def borrar_mascotas(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        mascota = Mascota.objects.filter(id=int(identificador)).first()
        if mascota:
            mascota.delete()
        return HttpResponseRedirect(reverse("index_mascotas"))
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar_mascotas(request, identificador=''):
    '''
    TODO: implementar una vista para actualización
    '''
    if request.method == "GET":
        mascota = get_object_or_404(Mascota, pk=int(identificador))
        initial = {
            "id": mascota.id,
            "nombre": mascota.nombre, 
            "tipo": mascota.tipo, 
            "edad": mascota.edad,
            "peso": mascota.peso,
        }
    
        form_actualizar = ActualizarMascotaForm(initial=initial)
        return render(request, 'mascotas/form_mascotas_carga.html', {'form': form_actualizar, 'actualizar': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarMascotaForm(request.POST)
        if form_actualizar.is_valid():
            mascota = get_object_or_404(Mascota, pk=form_actualizar.cleaned_data['id'])
            mascota.nombre = form_actualizar.cleaned_data['nombre']
            mascota.tipo = form_actualizar.cleaned_data['tipo']
            mascota.edad = form_actualizar.cleaned_data['edad']
            mascota.peso = form_actualizar.cleaned_data['peso']
            mascota.save()

            return HttpResponseRedirect(reverse("index_mascotas"))


def buscar_mascotas(request):
    
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarMascotasForm(request.GET)
        if form_busqueda.is_valid():
            mascotas = Mascota.objects.filter(nombre__icontains=request.GET.get("palabra_a_buscar"))
            return  render(request, 'mascotas/lista_mascotas.html', {"mascotas": mascotas, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarMascotasForm()
        return render(request, 'mascotas/form_mascotas_busqueda.html', {"form_busqueda": form_busqueda})
        
    