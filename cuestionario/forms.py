from django import forms

class CuestionarioForm(forms.Form):

    universidad = forms.ChoiceField(
        label="¿De que universidad eres?",
        help_text="Selecciona la institución a la que perteneces.",
        choices=[
            ("utfsm", "Universidad Técnica Federico Santa María"),
            ("pucv", "Pontificia Universidad Católica de Valparaíso (AUN NO IMPLEMENTADO)"),
        ],
        widget=forms.RadioSelect
    )

    categoria = forms.ChoiceField(
        label="Elige la categoría de tu problema",
        help_text="Selecciona la opción que mejor describa la situación que estás experimentando.",
        choices=[
            ("academico", "Problemas Académicos (notas, evaluaciones, asignaturas)"),
            ("administrativo", "Problemas Administrativos (matrícula, certificados, trámites)"),
            ("discriminacion", "Discriminación (trato desigual o exclusión)"),
            ("acoso", "Acoso Académico (hostigamiento por docentes o estudiantes)"),
            ("economico", "Problemas Económicos (becas, aranceles o falta de recursos)"),
        ],
        widget=forms.RadioSelect
    )

    objetivo = forms.ChoiceField(
        label="¿Cuál es tu objetivo?",
        help_text="Indica qué tipo de ayuda o resultado esperas obtener respecto de la situación descrita.",
        choices=[
            ("solucion", "Buscar una solución al problema"),
            ("orientacion", "Recibir orientación o recursos que me puedan ayudar"),
            ("contacto", "Saber a qué unidad o persona debo contactar"),
            ("denuncia", "Conocer los canales para realizar una denuncia"),
        ],
        widget=forms.RadioSelect
    )