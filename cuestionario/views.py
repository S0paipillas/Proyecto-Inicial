from django.shortcuts import render, redirect
from .forms import CuestionarioFormPag1, CuestionarioFormPag2
from .models import Orientacion

SUBCATEGORIAS = {
    "academico": [
        ("notas", "Notas"),
        ("evaluaciones", "Evaluaciones"),
        ("inscripciones", "Inscripción de asignaturas"),
    ],

    "administrativo": [
        ("matricula", "Matrícula"),
        ("certificados", "Certificados"),
        ("tramites", "Trámites"),
    ],

    "economico": [
        ("becas", "Becas"),
        ("aranceles", "Aranceles"),
        ("beneficios", "Beneficios estudiantiles"),
    ],

    "acoso": [
        ("docente", "Acoso por docente"),
        ("estudiante", "Acoso por estudiante"),
    ],

    "discriminacion": [
        ("genero", "Discriminación por género"),
        ("otro", "Otro tipo de discriminación"),
    ]
}


def cuestionariopaso1(request):
    """Paso 1"""

    if request.method == "POST":
        form = CuestionarioFormPag1(request.POST)

        if form.is_valid():

            request.session["universidad"] = form.cleaned_data["universidad"]
            request.session["conflicto"] = form.cleaned_data["conflicto"]

            return redirect("paso2")

    else:
        form = CuestionarioFormPag1()

    return render(
        request,
        "cuestionario/cuestionario.html",
        {"form": form}
    )


def cuestionariopaso2(request):

    conflicto = request.session.get("conflicto")

    if not conflicto:
        return redirect("cuestionario")

    form = CuestionarioFormPag2(request.POST or None)

    form.fields["subconflicto"].choices = SUBCATEGORIAS[conflicto]

    if request.method == "POST" and form.is_valid():

        subconflicto = form.cleaned_data["subconflicto"]
        derechos = form.cleaned_data["derechos"]

        universidad = request.session.get("universidad")

        orientacion = Orientacion.objects.filter(
            universidad__codigo=universidad,
            conflicto__codigo=conflicto,
            subconflicto__codigo=subconflicto,
            derechos__codigo=derechos,
        ).first()

        return render(
            request,
            "cuestionario/resultado.html",
            {
                "orientacion": orientacion,
            }
        )

    return render(
        request,
        "cuestionario/cuestionario.html",
        {"form": form}
    )