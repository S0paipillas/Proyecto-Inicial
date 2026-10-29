from django.shortcuts import render
from .forms import CuestionarioForm

def cuestionario(request):

    if request.method == "POST":
        form = CuestionarioForm(request.POST)

        if form.is_valid():

            universidad_seleccionada = form.cleaned_data["universidad"]
            categoria_seleccionada = form.cleaned_data["categoria"]
            objetivo_seleccionado = form.cleaned_data["objetivo"]

            return render(
                request,
                "cuestionario/resultado.html",
                {
                    "universidad": universidad_seleccionada,
                    "categoria": categoria_seleccionada,
                    "objetivo": objetivo_seleccionado,
                }
            )

    else:
        form = CuestionarioForm()

    return render(
        request,
        "cuestionario/cuestionario.html",
        {"form": form}
    )