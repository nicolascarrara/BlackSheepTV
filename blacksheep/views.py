from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from BlackSheepTV import settings
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from blacksheep.models import Film, Serie,Saison,Episode
import requests
import urllib
import json

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
    req.add_header('Authorization','Bearer '+request.session['tokenapi'])
    resp = urllib.request.urlopen(req)
    content = resp.read()
    return HttpResponse(content)

class FilmListView(ListView):
    model = Film

    def get_context_data(self, **kwargs):
        context = super(FilmListView, self).get_context_data(**kwargs)
        context['templates'] = "blacksdataheep/listFilm.html"
        return context


class SerieListView(ListView):
    model = Serie

    def get_context_data(self, **kwargs):
        context = super(SerieListView, self).get_context_data(**kwargs)
        context['templates'] = "serie_list.html"
        return context


class FilmDetailView(DetailView):
    model = Film
    template_name = "blacksheep/film_detail.html"


class SerieDetailView(DetailView):
    model = Serie
    template_name = "blacksheep/serie_detail.html"


class SaisonDetailView(DetailView):
    model = Saison
    template_name = "blacksheep/detailSaison.html"


class EpisodeDetailView(DetailView):
    model = Episode
    template_name = "blacksheep/detailEpisode.html"


def rechercheFilm(request):

    query = request.GET.get('query')
    content=''

    if not query:

        films = Film.objects.all()

    else:

        films = Film.objects.filter(titre=query)

        if not films.exists():

            query = urllib.request.pathname2url(query)
            req = urllib.request.Request('https://api.themoviedb.org/3/search/movie?api_key=e1bf1e9eda0b0070cc6a8ff1796ca8ec&language=fr&query='+query)
            resp = urllib.request.urlopen(req)
            string = resp.read().decode('utf-8')
            content = json.loads(string)
            #films=content['data'][0]
            films=[]
            for film in content['results']:
                movie=Film()
                movie.titre=film['title']
                movie.id=film['id']
                movie.image=film['poster_path']
                movie.note=film['vote_average']
                movie.synopsis=film['overview']
                films.append(movie)
                if Film.objects.filter(id=movie.id):
                    pass
                else:
                    query = Film(id = movie.id , titre = movie.titre ,image= movie.image,synopsis=movie.synopsis,note=movie.note)
                    query.save()


    title = "Résultats pour la requête %s"%query

    context = {

        'films': films

    }
    return render(request, 'blacksheep/film_search.html', context)

def rechercheSerie(request):
    series=""
    query = request.GET.get('query')
    content = ''
    if not query:
        series = Serie.objects.all()
    else:
        #series = Serie.objects.filter(seriesName=query)
        query = urllib.request.pathname2url(query)
        req = urllib.request.Request('https://api.thetvdb.com/search/series?name='+query)
        req.add_header('Accept', 'application/json')
        req.add_header('Accept-Language', 'fr')
        req.add_header('Authorization','Bearer '+request.session['tokenapi'])
        try:
            resp = urllib.request.urlopen(req)
            test='ok'

        except Exception as e:
            test=False
        if(test!='ok'):
            pass
        else:
            string = resp.read().decode('utf-8')
            content = json.loads(string)
            series=[]
            for serie in content['data']:
                tvserie=Serie()
                tvserie.id=serie['id']
                tvserie.seriesName=serie['seriesName']
                tvserie.network=serie['network']
                tvserie.overview=serie['overview']
                tvserie.status=serie['status']
                tvserie.banner=serie['banner']
                tvserie.firstAired=serie['firstAired']
                series.append(tvserie)
                if Serie.objects.filter(id=tvserie.id):
                    pass
                else:
                    query = Serie(firstAired = tvserie.firstAired , id = tvserie.id, network=tvserie.network , overview= tvserie.overview,seriesName=tvserie.seriesName,status=tvserie.status ,banner=tvserie.banner )
                    query.save()

    title = "Résultats pour la requête %s"%query
    if series=='':
        series=""
        #series = Serie.objects.all()
    context = {

        'series': series

    }
    return render(request, 'blacksheep/serie_search.html', context)
