from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import InscriptionForm

# Create your views here.
def index(request):
    return render(request, "formulaire/index.html")

class InscriptionView(CreateView):
    template_name = 'inscription.html'
    form_class = InscriptionForm
    success_url = '/merci/'