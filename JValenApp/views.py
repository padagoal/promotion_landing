from django.shortcuts import render
from .models import Personas_votante
# Create your views here.


def home(request):
    return render(request, "home.html", {})


def reporteVotante(request):
    numero = request.GET.get('dato')
    filtro = request.GET.get('filtro')

    try:
        if(filtro == 'cedula'):
            datoVotante = Personas_votante.objects.get(cedula__exact=numero)

        else:
            datoVotante = Personas_votante.objects.get(matricula__exact=numero)

        return render(request, "resultado.html", {'datoVotante':datoVotante})
    except Exception as e:

        return render(request, "resultado.html", {})


def reporteVotanteInterno(request):
    numero = request.GET.get('dato')
    filtro = request.GET.get('filtro')


    if(filtro == 'cedula'):
        datoVotante = Personas_votante.objects.get(cedula__exact=numero)

    else:
        datoVotante = Personas_votante.objects.get(matricula__exact=numero)

    return render(request, "resultadoInterno.html", {'datoVotante':datoVotante})