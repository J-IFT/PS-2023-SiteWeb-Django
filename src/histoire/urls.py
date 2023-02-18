from django.urls import path
from .views import chap

urlpatterns = [
    path('chap-<str:numero_chap>/', chap, name="histoire-chap1"),
]