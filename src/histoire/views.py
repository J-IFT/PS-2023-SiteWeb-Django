from django.shortcuts import render


def chap(request, numero_chap):
    print(numero_chap)
    return render(request, "histoire/chap1.html")


