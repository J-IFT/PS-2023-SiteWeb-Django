from django import forms
from django.contrib.auth.models import User

class NewUserForm(forms.Form):
    username = forms.CharField(label='Nom', max_length=100)
    # email = forms.CharField(label='Email', max_length=100)
    user = User.objects.create_user(username, 'test@test.com', 'password')
    user.save()

class LoginForm(forms.Form):
    username = forms.CharField(label='Nom', max_length=100)
    password = forms.CharField(label='MDP', max_length=100)
