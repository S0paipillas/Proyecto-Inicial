from django import forms

class CuestionarioForm(forms.Form):

    universidad = forms.ChoiceField(
        label="¿De que universidad eres?",
        help_text="Selecciona la institución a la que perteneces.",
        choices=[
            ("utfsm", "Universidad Tecnica Federico Santa Maria"),
        ],
        widget=forms.RadioSelect
    )

    categoria = forms.ChoiceField(
        label="Elige la categoría de tu problema",
        help_text="Selecciona la opción que mejor describa la situación que estás experimentando.",
        choices=[
            ("academico", "Problemas Académicos"),
            ("administrativo", "Problemas Administrativos"),
            ("discriminacion", "Discriminación"),
            ("acoso", "Acoso Académico"),
            ("economico", "Problemas Económicos"),
        ],
        widget=forms.RadioSelect
    )

    objetivo = forms.ChoiceField(
        label="¿Cuál es tu objetivo?",
        help_text="Indica qué tipo de ayuda o resultado esperas obtener respecto de la situación descrita.",
        choices=[
            ("solucion", "Buscar una solución al problema"),
            ("orientacion", "Recibir orientación o recursos que me puedan ayudar"),
        ],
        widget=forms.RadioSelect
    )