from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("formulaire/connexion.html")
        messages.error(request, form.errors)
    form = NewUserForm()
    return render (request, "formulaire/index.html", {"form":form})

def connexion(request):
    return render(request, "formulaire/connexion.html")