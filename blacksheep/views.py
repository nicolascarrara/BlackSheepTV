from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from BlackSheepTV import settings
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from blacksheep.models import Film, Serie,Saison,Episode
import requests

# Create your views here.


def accueil(request):
    return render(request, 'blacksheep/accueil.html')


def test(request):
    parameters ={"apikey": "C9D85668BADC5AD4","userkey": "04565F600F78B2C0","username": "nicolascarrara"}
    response = requests.post(
        "https://api.thetvdb.com/login", json=parameters)
    data = response.json()
    return HttpResponse(data['token'])

class FilmListView(ListView):
    model = Film

    def get_context_data(self, **kwargs):
        context = super(FilmListView, self).get_context_data(**kwargs)
        context['templates'] = "blacksheep/listFilm.html"
        return context


class SerieListView(ListView):
    model = Serie

    def get_context_data(self, **kwargs):
        context = super(SerieListView, self).get_context_data(**kwargs)
        context['templates'] = "blacksheep/listSerie.html"
        return context


class FilmDetailView(DetailView):
    model = Film
    template_name = "blacksheep/detailFilm.html"


class SerieDetailView(DetailView):
    model = Serie
    template_name = "blacksheep/detailSerie.html"


class SaisonDetailView(DetailView):
    model = Saison
    template_name = "blacksheep/detailSaison.html"


class EpisodeDetailView(DetailView):
    model = Episode
    template_name = "blacksheep/detailEpisode.html"
