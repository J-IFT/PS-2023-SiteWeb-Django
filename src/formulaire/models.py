# Create your models here.
from .models import Utilisateur
from django import forms
from django.db import models



class Utilisateur(models.Model):
    pseudo = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mdp = models.CharField(max_length=50)
