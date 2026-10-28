from django.shortcuts import render
from .forms import CuestionarioForm

def cuestionario(request):

    if request.method == "POST":
        form = CuestionarioForm(request.POST)

        if form.is_valid():

            universidad = form.cleaned_data["universidad"]
            categoria = form.cleaned_data["categoria"]
            objetivo = form.cleaned_data["objetivo"]

            print(universidad) # para debuggear , quitar despues
            print(categoria)
            print(objetivo)

            return render(
                request,
                "cuestionario/resultado.html",
                {
                    "universidad": universidad,
                    "categoria": categoria,
                    "objetivo": objetivo,
                }
            )

    else:
        form = CuestionarioForm()

    return render(
        request,
        "cuestionario/cuestionario.html",
        {"form": form}
    )