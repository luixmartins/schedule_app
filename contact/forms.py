from django import forms 
from django.core.exceptions import ValidationError 

from .models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ), 
        label='Primeiro Nome', 
        help_text='Texto de ajuda para o usuário', 
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.fields['first_name'].widget.attrs.update({
        #    'class': 'classe-a classe-b', 
        #    'placeholder': 'Escreva Aqui', 
        #})

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category', 
            )
        #widgets = {
        #    'first_name': forms.TextInput(attrs={
        #        'class': 'classe-a', 
        #    }) 
        #}

    def clean(self):
        #cleaned_data = self.cleaned_data 
        
        #self.add_error(
        #    'first_name', 
         #   ValidationError(
         #       'Mensagem de erro', 
         #       code='invalid'
         #   )
        #)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name', 
                ValidationError(
                'vEIO DO ADD ERROR', 
                code='invalid'
                )
            )
        return first_name