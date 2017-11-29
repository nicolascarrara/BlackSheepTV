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


def loginAPI(request):
    parameters ={"apikey": "C9D85668BADC5AD4","userkey": "04565F600F78B2C0","username": "nicolascarrara"}
    response = requests.post(
        "https://api.thetvdb.com/login", json=parameters)
    data = response.json()
    request.session['tokenapi'] = data['token']
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



def rechercheFilm(request):

    query = request.GET.get('query')

    if not query:

        films = Film.objects.all()

    else:

        films = Film.objects.filter(titre_icontains=query)

    """if not films.exists():

        films = Film.objects.filter(realisateur__icontains=query)"""

    title = "Résultats pour la requête %s"%query

    context = {

        'films': films

    }

    return render(request, 'blacksheep/film_search.html', context)

def rechercheSerie(request):

    query = request.GET.get('query')

    if not query:

        series = Serie.objects.all()

    else:

        series = Serie.objects.filter(titre_icontains=query)

    """if not films.exists():

        films = Film.objects.filter(realisateur__icontains=query)"""

    title = "Résultats pour la requête %s"%query

    context = {

        'series': series

    }

    return render(request, 'blacksheep/serie_search.html', context)