from django.shortcuts import render
from django.http import HttpResponse

def recursos(request):
    return render(request, "recursos/recursos.html")

def derechos_estudiantiles(request):
    return render(request, "recursos/derechos_estudiantiles.html")