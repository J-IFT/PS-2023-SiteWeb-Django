from django.shortcuts import render


def index(request):
    return render(request, "histoire/index.html")

def chap(request, numero_chap):
    return render(request, "histoire/chap1.html")