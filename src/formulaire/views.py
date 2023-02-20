from django.shortcuts import  render, redirect
from .forms import NewUserForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NewUserForm()
    return render (request, "formulaire/index.html", {"form":form})

def connexion(request):
    if request.method == "GET":
        form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
    return render(request, "formulaire/connexion.html", {"form":form})