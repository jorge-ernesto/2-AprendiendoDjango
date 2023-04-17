from django import forms
from django.core import validators

class FormArticle(forms.Form):
    # Definir los datos de la clase (inputs del formulario)
    # Si no se especifica lo contrario, todos los inputs seran required=TRUE por defecto
    title = forms.CharField(
        label = "Titulo",  # Esto es lo que se mostrara en el label del formulario
        max_length = 20,
        required = True,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Mete el titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators = [
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'El titulo esta mal formado', 'invalid_title')
        ]
    )

    content = forms.CharField(
        label = "Contenido",  # Esto es lo que se mostrara en el label del formulario
        widget = forms.Textarea,
        # widget = forms.Textarea(
        #     attrs={
        #         'placeholder': 'Mete el contenido YAA',
        #         'class': 'contenido_form_article',
        #         'id': 'contenido_form'
        #     }
        # ),
        validators = [
            validators.MaxLengthValidator(50, 'Te has pasado, has puesto mucho texto')
        ]
    )
    content.widget.attrs.update({
        'placeholder': 'Mete el contenido YAA',
        'class': 'contenido_form_article',
        'id': 'contenido_form'
    })

    public_options = [
        (1, "Si"),
        (0, "No")
    ]
    public = forms.TypedChoiceField(
        label = "¿Publicado?",  # Esto es lo que se mostrara en el label del formulario
        choices = public_options,
    )
