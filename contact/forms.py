from django import forms 
from django.core.exceptions import ValidationError 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

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
    

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True 
    )
    class Meta:
        model = User 
        fields = (
            'first_name', 'last_name', 'email', 
            'username', 'password1', 'password2', 
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', 
                ValidationError('This email already exists', code='invalid')
            )

        return email 