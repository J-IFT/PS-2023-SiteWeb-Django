from django.urls import path
from .views import chap
from .views import index

urlpatterns = [
    path('', index, name="histoire-index"),
    path('chap1', chap, name="histoire-chap1"),
]