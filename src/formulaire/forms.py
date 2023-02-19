from django import forms
from .models import Utilisateur

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['pseudo', 'email', 'mdp']
        widgets = {
            'mdp': forms.PasswordInput()
        }