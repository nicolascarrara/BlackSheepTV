from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from BlackSheepTV import settings
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from blacksheep.models import Film, Serie,Saison,Episode
import requests
import urllib

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

def search(request):
    req = urllib.request.Request('https://api.thetvdb.com/search/series?name=Breaking%20Bad')
    req.add_header('Accept', 'application/json')
    req.add_header('Accept-Language', 'fr')
    req.add_header('Authorization','Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTIwNjA5NzUsImlkIjoiQmxhY2tTaGVlcFRWIiwib3JpZ19pYXQiOjE1MTE5NzQ1NzUsInVzZXJpZCI6NDkwMTk4LCJ1c2VybmFtZSI6Im5pY29sYXNjYXJyYXJhIn0.ihUfnS-288J8hTSbDhdJyfBijjCfn2EfoSYtxSzFQIFbtRs2hkKzR05Xw0_dhg4u-Udp7rx-PyGyWnOpvcr0yXYv996OIBZhc9eOXDwuo9ARHOcXBNqeo5V7oJR_yqgjDUCupeewbg6OTlSfXadWwihSJBG1D8fW5j7jRP39Qkwu0kUKYEXIrxy9fKqL_pZBgR2qZnjpDpjAHYTE-CeR47N0Je-rrxeJgi8nJD_TMtI-fGlZze8QUmt-lYTn--_q84YCvaktlwaEFmvSeZU3tB56XqIgX48kqVWE0eT_D0tM-3LLNvptWtlumjl1Navc1kseOPolj_gleI23KooKxw')
    resp = urllib.request.urlopen(req)
    content = resp.read()
    return HttpResponse(content)

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

def serieAPI(nom):
    context=nom

def rechercheSerie(request):

    query = request.GET.get('query')
    series=''

    if not query:

        search(request)

    else:
        query=urllib.request.pathname2url(query)
        req = urllib.request.Request('https://api.thetvdb.com/search/series?name='+query)
        req.add_header('Accept', 'application/json')
        req.add_header('Accept-Language', 'fr')
        req.add_header('Authorization','Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTIwNjA5NzUsImlkIjoiQmxhY2tTaGVlcFRWIiwib3JpZ19pYXQiOjE1MTE5NzQ1NzUsInVzZXJpZCI6NDkwMTk4LCJ1c2VybmFtZSI6Im5pY29sYXNjYXJyYXJhIn0.ihUfnS-288J8hTSbDhdJyfBijjCfn2EfoSYtxSzFQIFbtRs2hkKzR05Xw0_dhg4u-Udp7rx-PyGyWnOpvcr0yXYv996OIBZhc9eOXDwuo9ARHOcXBNqeo5V7oJR_yqgjDUCupeewbg6OTlSfXadWwihSJBG1D8fW5j7jRP39Qkwu0kUKYEXIrxy9fKqL_pZBgR2qZnjpDpjAHYTE-CeR47N0Je-rrxeJgi8nJD_TMtI-fGlZze8QUmt-lYTn--_q84YCvaktlwaEFmvSeZU3tB56XqIgX48kqVWE0eT_D0tM-3LLNvptWtlumjl1Navc1kseOPolj_gleI23KooKxw')
        resp = urllib.request.urlopen(req)
        content = resp.read()
        #series = content
        return HttpResponse(content)

    #if not series.exists():



    title = "Résultats pour la requête %s"%query

    context = {

        'series': query

    }

    return render(request, 'blacksheep/serie_search.html', context)
