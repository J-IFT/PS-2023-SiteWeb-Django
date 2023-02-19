from django.urls import path
from .views import index
from .views import connexion

urlpatterns = [
    path('', index, name="formulaire-index"),
    path('connexion', connexion, name="formulaire-connexion"),
]