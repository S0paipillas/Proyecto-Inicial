from django.shortcuts import render

def cuestionario(request):
    return render(request, 'cuestionario/cuestionario.html')