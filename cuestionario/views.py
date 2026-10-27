from django.shortcuts import render
from .forms import CuestionarioForm

def cuestionario(request):
    form = CuestionarioForm()

    return render(
        request,
        "cuestionario/cuestionario.html",
        {"form": form}
    )