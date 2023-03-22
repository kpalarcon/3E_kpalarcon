from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo, Trofeo, Torneo
from .forms import EquipoForm, BuscarEquipoForm, BuscarTrofeoForm, TrofeoForm, BuscarTorneoForm, TorneoForm
from django.db.models import Q
from django.contrib import messages


def crear_equipo(request):
    if request.method == "POST":
        equipoForm = EquipoForm(request.POST or None)
        if equipoForm.is_valid():
            nombreequipo = equipoForm.cleaned_data['nombreequipo']
            usuario_creacion = request.user
            usuario_modificacion = request.user
            Equipo.objects.create(nombreequipo=nombreequipo,usuario_creacion=usuario_creacion,
                                   usuario_modificacion=usuario_modificacion)
            messages.add_message(request, messages.SUCCESS, 'Su resgistro fue un existo')
            return redirect('consultar_equipo')
        else:
            messages.add_message(request, messages.WARNING, "No se registro exitosamente")
            equipoForm = EquipoForm()
    else:
        equipoForm = EquipoForm()
    return render(request, "equipo/crear_equipo.html", {"form": equipoForm})



def modificar_equipo(request, id):
    if request.method == "POST":
        equipo = get_object_or_404(Equipo, pk=id)
        equipoForm = EquipoForm(request.POST or None, instance=equipo)
        if equipoForm.is_valid():
            Equipo.usuario_modificacion = request.user
            equipoForm.save()
            return redirect('consultar_equipo')
    else:  # GET
        equipo = get_object_or_404(Equipo, pk=id)
        equipoForm = EquipoForm(instance=equipo)
    return render(request, "equipo/modificar_equipo.html", {'form': equipoForm})

def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, pk=id)
    if request.method == "POST":
        equipoForm = EquipoForm(request.POST, instance=equipo)
        if equipoForm.is_valid():
            equipo.usuario_modificacion = request.user
            equipo.estado = 0
            equipo.save()
            messages.add_message(request, messages.SUCCESS, "SU REGISTRO SE ELIMINO EXITOSAMENTE!")
            return redirect('consultar_equipo')
    else:  # GET
        equipoForm = EquipoForm(instance=equipo)
    return render(request, "equipo/eliminar_equipo.html", {'form': equipoForm})




def consultar_equipo(request):
    equipos = Equipo.objects.filter(estado=1)
    buscarEquipo = BuscarEquipoForm()
    return render(request, "equipo/consultar_equipo.html", {"lista_equipos": equipos, 'buscar_equipo': buscarEquipo})


def buscar_equipo(request):
    if request.method == "POST":
        buscarEquipo = BuscarEquipoForm(request.POST or None)
        if buscarEquipo.is_valid():
            desde = buscarEquipo.cleaned_data['desde']
            hasta = buscarEquipo.cleaned_data['hasta']
            equipos = Equipo.objects.filter(fecha_creacion__range=(desde, hasta))
        else:
            buscarEquipo = BuscarEquipoForm()
        return render(request, "equipo/consultar_equipo.html", {"lista_equipos": equipos, 'buscar_equipo': buscarEquipo})


def crear_trofeo(request):
    if request.method == "POST":
        trofeoForm = TrofeoForm(request.POST or None)
        if trofeoForm.is_valid():
            trofeoForm.save()
            return redirect("consultar_trofeo")
    else:
        trofeoForm = TrofeoForm
    return render(request, "trofeo/crear_trofeo.html", {"form": trofeoForm})


def modificar_trofeo(request, id):
    if request.method == "POST":
        trofeo = get_object_or_404(Trofeo, pk=id)
        trofeoForm = TrofeoForm(request.POST or None, instance=trofeo)
        if trofeoForm.is_valid():
            trofeoForm.save()
            return redirect('consultar_trofeo')
    else:  # GET
        trofeo = get_object_or_404(Trofeo, pk=id)
        trofeoForm = TrofeoForm(instance=trofeo)
    return render(request, "trofeo/modificar_trofeo.html", {'form': trofeoForm})


def eliminar_trofeo(request, id):
    if request.method == "POST":
        trofeo = get_object_or_404(Trofeo, pk=id)
        trofeoForm = TrofeoForm(request.POST or None, instance=trofeo)
        if trofeoForm.is_valid():
            trofeoForm.save(commit=False)
            trofeo.estado = 0
            trofeoForm.save(commit=True)
            return redirect('consultar_trofeo')
    else:  # GET
        trofeo = get_object_or_404(Trofeo, pk=id)
        trofeoForm = TrofeoForm(instance=trofeo)
    return render(request, "trofeo/eliminar_trofeo.html", {'form': trofeoForm})


def consultar_trofeo(request):
    trofeos = Trofeo.objects.filter(estado=1)
    buscartrofeo = BuscarTrofeoForm()
    return render(request, "trofeo/consultar_trofeo.html", {"lista_trofeos": trofeos, 'buscar_trofeo': buscartrofeo})


def buscar_trofeo(request):
    if request.method == "POST":
        buscarTrofeo = BuscarTrofeoForm(request.POST or None)
        if buscarTrofeo.is_valid():
            desde = buscarTrofeo.cleaned_data['desde']
            hasta = buscarTrofeo.cleaned_data['hasta']
            trofeos = Trofeo.objects.filter(fecha_creacion__range=(desde, hasta))
    return render(request, "trofeo/consultar_trofeo.html", {"lista_trofeos": trofeos, 'buscar_trofeo': buscarTrofeo})


def crear_torneo(request):
    if request.method == "POST":
        torneoForm = TorneoForm(request.POST or None)
        if torneoForm.is_valid():
            torneoForm.save()
            return redirect("consultar_torneo")
    else:
        torneoForm = TorneoForm
    return render(request, "torneo/crear_torneo.html", {"form": torneoForm})


def modificar_torneo(request, id):
    if request.method == "POST":
        torneo = get_object_or_404(Torneo, pk=id)
        torneoForm = TorneoForm(request.POST or None, instance=torneo)
        if torneoForm.is_valid():
            torneoForm.save()
            return redirect('consultar_torneo')
    else:  # GET
        torneo = get_object_or_404(Torneo, pk=id)
        torneoForm = TorneoForm(instance=torneo)
    return render(request, "torneo/modificar_torneo.html", {'form': torneoForm})


def eliminar_torneo(request, id):
    if request.method == "POST":
        torneo = get_object_or_404(Torneo, pk=id)
        torneoForm = TorneoForm(request.POST or None, instance=torneo)
        if torneoForm.is_valid():
            torneoForm.save(commit=False)
            torneo.estado = 0
            torneoForm.save(commit=True)
            return redirect('consultar_torneo')
    else:  # GET
        torneo = get_object_or_404(Torneo, pk=id)
        torneoForm = TorneoForm(instance=torneo)
    return render(request, "torneo/eliminar_torneo.html", {'form': torneoForm})


def consultar_torneo(request):
    torneos = Torneo.objects.filter(estado=1)
    buscarTorneo = BuscarTorneoForm()
    return render(request, "torneo/consultar_torneo.html", {"lista_torneos": torneos, 'buscar_torneo': buscarTorneo})


def buscar_torneo(request):
    if request.method == "POST":
        buscarTorneo = BuscarTorneoForm(request.POST or None)
        if buscarTorneo.is_valid():
            equipo = buscarTorneo.cleaned_data['equipo']
            trofeo = buscarTorneo.cleaned_data['trofeo']
            desde = buscarTorneo.cleaned_data['desde']
            hasta = buscarTorneo.cleaned_data['hasta']
            torneos = Torneo.objects.filter(Q(equipo__nombreequipo__contains=equipo) & Q(trofeo__nombretrofeo__contains=trofeo) & Q(fecha_creacion__range=(desde, hasta)))
    else:
        buscarTorneo = BuscarTorneoForm()
    return render(request, "torneo/consultar_torneo.html", {"lista_torneos": torneos, 'buscar_torneo': buscarTorneo})
