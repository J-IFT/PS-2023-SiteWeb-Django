from django.shortcuts import render


def index(request):
    return render(request, "JDR/index.html", context={"prenom": "Patrick"})
