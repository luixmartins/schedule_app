from django import forms 
from django.core.exceptions import ValidationError 

from .models import Contact

class ContactForm(forms.ModelForm):

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',  
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