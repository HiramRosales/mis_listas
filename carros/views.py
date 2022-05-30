from readline import append_history_file
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from carros.forms import CarroForm, BuscarCarrosForm, ActualizarCarroForm

from carros.models import Carro

def index_carro(request):
    carros = Carro.objects.all()
    template = loader.get_template('carros/lista_carros.html')
    context = {
        'carros': carros,
    }
    return HttpResponse(template.render(context, request))


def agregar_carro(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = CarroForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            marca = form.cleaned_data['marca']
            ano_creacion = form.cleaned_data['ano_creacion']
            cap_lts = form.cleaned_data['cap_lts']
            Carro(nombre=nombre, marca=marca, ano_creacion=ano_creacion, cap_lts=cap_lts).save()

            return HttpResponseRedirect(reverse("index_carro"))
    elif request.method == "GET":
        form = CarroForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'carros/form_carro_carga.html', {'form': form})


def borrar_carro(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        carro = Carro.objects.filter(id=int(identificador)).first()
        if carro:
            carro.delete()
        return HttpResponseRedirect(reverse("index_carro"))
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar_carro(request, identificador=''):
    '''
    TODO: implementar una vista para actualización
    '''
    if request.method == "GET":
        carro = get_object_or_404(Carro, pk=int(identificador))
        initial = {
            "id": carro.id,
            "nombre": carro.nombre, 
            "marca": carro.marca, 
            "ano_creacion": carro.ano_creacion,
            "cap_lts": carro.cap_lts,
        }
    
        form_actualizar = ActualizarCarroForm(initial=initial)
        return render(request, 'carros/form_carro_carga.html', {'form': form_actualizar, 'actualizar': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarCarroForm(request.POST)
        if form_actualizar.is_valid():
            carro = get_object_or_404(Carro, pk=form_actualizar.cleaned_data['id'])
            carro.nombre = form_actualizar.cleaned_data['nombre']
            carro.marca = form_actualizar.cleaned_data['marca']
            carro.ano_creacion = form_actualizar.cleaned_data['ano_creacion']
            carro.cap_lts = form_actualizar.cleaned_data['cap_lts']
            carro.save()

            return HttpResponseRedirect(reverse("index_carro"))


def buscar_carro(request):
    
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarCarrosForm(request.GET)
        if form_busqueda.is_valid():
            carros = Carro.objects.filter(nombre__icontains=request.GET.get("palabra_a_buscar"))
            return  render(request, 'carros/lista_carros.html', {"carros": carros, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarCarrosForm()
        return render(request, 'carros/form_carro_busqueda.html', {"form_busqueda": form_busqueda})
        
    