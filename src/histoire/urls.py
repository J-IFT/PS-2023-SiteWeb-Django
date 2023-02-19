from django.urls import path
from .views import index
from .views import chap
from .views import chap2
from .views import chap3
from .views import chap4
from .views import chap5
from .views import chap6
from .views import chap7
from .views import chap8
from .views import chap9
from .views import chap10
from .views import chap11
from .views import chap12
from .views import chap13
from .views import chap14
from .views import chap15
from .views import chap16

urlpatterns = [
    path('', index, name="histoire-index"),
    path('chap1', chap, name="histoire-chap1"),
    path('chap2', chap2, name="histoire-chap2"),
    path('chap3', chap3, name="histoire-chap3"),
    path('chap4', chap4, name="histoire-chap4"),
    path('chap5', chap5, name="histoire-chap5"),
    path('chap6', chap6, name="histoire-chap6"),
    path('chap7', chap7, name="histoire-chap7"),
    path('chap8', chap8, name="histoire-chap8"),
    path('chap9', chap9, name="histoire-chap9"),
    path('chap10', chap10, name="histoire-chap10"),
    path('chap11', chap11, name="histoire-chap11"),
    path('chap12', chap12, name="histoire-chap12"),
    path('chap13', chap13, name="histoire-chap13"),
    path('chap14', chap14, name="histoire-chap14"),
    path('chap15', chap15, name="histoire-chap15"),
    path('chap16', chap16, name="histoire-chap16"),
]