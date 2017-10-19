from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
# Create your views here.


def accueil(request):
    return render(request, 'blacksheep/accueil.html')
