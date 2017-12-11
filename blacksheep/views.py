from django.shortcuts import render
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from BlackSheepTV import settings
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from blacksheep.models import Film, Serie,Saison,Episode,Genre
import requests,string,urllib,json,time
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

def discoverAPI(request):
    req = urllib.request.Request('https://api.themoviedb.org/3/genre/movie/list?api_key=e1bf1e9eda0b0070cc6a8ff1796ca8ec&language=fr')
    resp = urllib.request.urlopen(req)
    string = resp.read().decode('utf-8')
    content = json.loads(string)
    for genree in content['genres']:
        genre=Genre()
        genre.name=genree['name']
        genre.id=genree['id']
        if Genre.objects.filter(name=genre.name):
            pass
        else:
            query = Genre(name = genre.name, id=genre.id)
            query.save()

    req = urllib.request.Request('https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&language=fr&api_key=e1bf1e9eda0b0070cc6a8ff1796ca8ec')
    resp = urllib.request.urlopen(req)
    string = resp.read().decode('utf-8')
    content = json.loads(string)
    films=[]
    i=0
    for film in content['results']:
        if i<18:
            i=i+1
            movie=Film()
            j=0
            for genre in film['genre_ids']:
                if j==0:
                    movie.genre=genre
                    j=j+1
                else:
                    movie.genre=str(movie.genre)+'/'+str(genre)
            movie.titre=film['title']
            movie.id=film['id']
            movie.image=film['poster_path']
            movie.note=film['vote_average']
            movie.synopsis=film['overview']
            movie.date_sortie=film['release_date']
            films.append(movie)
            if Film.objects.filter(id=movie.id):
                pass
            else:
                query = Film(id = movie.id , titre = movie.titre ,image= movie.image,synopsis=movie.synopsis,note=movie.note,genre=movie.genre,date_sortie=movie.date_sortie)
                query.save()
    context = {

        'object_list': films

    }
    return render(request, 'blacksheep/v_filmList.html', context)

def FilmList(request):
    films_list = Film.objects.all()
    film_form=[]
    #filmyear=forms.ModelChoiceField(queryset=Film.objects.values_list('date_sortie', flat = True).distinct(), empty_label="Année de sortie")
    list_genre = Genre.objects.all()
    paginator = Paginator(films_list, 18)
    page = request.GET.get('page')
    try:
        films = paginator.page(page)
    except PageNotAnInteger:
        films = paginator.page(1)
    except EmptyPage:
        films = paginator.page(paginator.num_pages)

    return render(request, 'blacksheep/film_list.html', {'object_list': films,'range':paginator.page_range,'genres':list_genre})



def SerieList(request):
    series_list = Serie.objects.all()
    paginator = Paginator(series_list, 10)
    page = request.GET.get('page')
    try:
        series = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        series = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        series = paginator.page(paginator.num_pages)

    return render(request, 'blacksheep/serie_list.html', {'object_list': series, 'range':paginator.page_range})

class FilmDetailView(DetailView):
    model = Film
    template_name = "blacksheep/film_detail.html"

    def get_object(self):
        object = super().get_object()
        i=0
        if object.genre!='' and object.genre!="\n":
            lesgenre=object.genre.split('/')
            for genre in lesgenre:
                if i==0:
                    object.genre = Genre.objects.get(id=genre).name
                    i=i+1
                else:
                    object.genre=str(object.genre)+' / '+str(Genre.objects.get(id=genre).name)
        else:
            object.genre=''
        return object


class SerieDetailView(DetailView):
    model = Serie
    template_name = "blacksheep/serie_detail.html"


class SaisonDetailView(DetailView):
    model = Film
    template_name = "blacksheep/saison_detail.html"


class EpisodeDetailView(DetailView):
    model = Film
    template_name = "blacksheep/episode_detail.html"


def rechercheFilm(request):
    liste_param=[]
    query = request.GET.get('query')
    querygenre = request.GET.get('genre')
    content=''
    liste_param.append(query)
    liste_param.append(querygenre)
    list_genre = Genre.objects.all()
    if not query and not querygenre:

        films = Film.objects.all()
        paramgenre=''

    elif not query and querygenre!='':
        films = Film.objects.filter(genre__contains=querygenre)
        paramgenre=Genre()
        paramgenre=Genre.objects.get(id=querygenre)
        liste_param.append(paramgenre)

    elif query and not querygenre:
        if not films.exists():
            query = urllib.request.pathname2url(query)
            req = urllib.request.Request('https://api.themoviedb.org/3/search/movie?api_key=e1bf1e9eda0b0070cc6a8ff1796ca8ec&language=fr&query='+query)
            resp = urllib.request.urlopen(req)
            string = resp.read().decode('utf-8')
            content = json.loads(string)
            films=[]
            for film in content['results']:
                movie=Film()
                i=0
                if querygenre != '':
                    if querygenre in film['genre_ids']:
                        for genre in film['genre_ids']:
                            if i==0:
                                movie.genre=genre
                                i=i+1
                            else:
                                movie.genre=str(movie.genre)+'/'+str(genre)
                        movie.titre=film['title']
                        movie.id=film['id']
                        movie.image=film['poster_path']
                        movie.note=film['vote_average']
                        movie.synopsis=film['overview']
                        movie.date_sortie=film['release_date']
                        films.append(movie)
                        if Film.objects.filter(id=movie.id):
                            pass
                        else:
                            query = Film(id = movie.id , titre = movie.titre ,image= movie.image,synopsis=movie.synopsis,note=movie.note,genre=movie.genre,date_sortie=movie.date_sortie)
                            query.save()
                else:
                    paramgenre=''
                    for genre in film['genre_ids']:
                        if i==0:
                            movie.genre=genre
                            i=i+1
                        else:
                            movie.genre=str(movie.genre)+'/'+str(genre)
                            movie.titre=film['title']
                            movie.id=film['id']
                            movie.image=film['poster_path']
                            movie.note=film['vote_average']
                            movie.synopsis=film['overview']
                            if film['release_date']=='':
                                    pass
                            else:
                                movie.date_sortie=film['release_date']
                            if movie not in (films):
                                films.append(movie)
                                if Film.objects.filter(id=movie.id):
                                    pass
                                else:
                                    query = Film(id = movie.id , titre = movie.titre ,image= movie.image,synopsis=movie.synopsis,note=movie.note,genre=movie.genre,date_sortie=movie.date_sortie)
                                    query.save()

    else:

        if querygenre != '':
            paramgenre=Genre()
            paramgenre=Genre.objects.get(id=querygenre)
            liste_param.append(paramgenre)
            films = Film.objects.filter(titre__icontains=query,genre__contains=querygenre)
            if films=='':
                films = Film.objects.filter(titre__icontains=query,genre__contains='%'+querygenre)
            if films=='':
                films = Film.objects.filter(titre__icontains=query,genre__contains='%'+querygenre+'%')
            if films=='':
                films = Film.objects.filter(titre__icontains=query,genre__contains=querygenre+'%')
        else :
            films = Film.objects.filter(titre__icontains=query)
            paramgenre=''

        if not films.exists():

            query = urllib.request.pathname2url(query)
            req = urllib.request.Request('https://api.themoviedb.org/3/search/movie?api_key=e1bf1e9eda0b0070cc6a8ff1796ca8ec&language=fr&query='+query)
            resp = urllib.request.urlopen(req)
            string = resp.read().decode('utf-8')
            content = json.loads(string)
            films=[]
            for film in content['results']:
                movie=Film()
                i=0
                if querygenre != '':
                    if querygenre in film['genre_ids']:
                        for genre in film['genre_ids']:
                            if i==0:
                                movie.genre=genre
                                i=i+1
                            else:
                                movie.genre=str(movie.genre)+'/'+str(genre)
                        movie.titre=film['title']
                        movie.id=film['id']
                        movie.image=film['poster_path']
                        movie.note=film['vote_average']
                        movie.synopsis=film['overview']
                        movie.date_sortie=film['release_date']
                        films.append(movie)
                        if Film.objects.filter(id=movie.id):
                            pass
                        else:
                            query = Film(id = movie.id , titre = movie.titre ,image= movie.image,synopsis=movie.synopsis,note=movie.note,genre=movie.genre,date_sortie=movie.date_sortie)
                            query.save()
                else:
                    paramgenre=''
                    for genre in film['genre_ids']:
                        if i==0:
                            movie.genre=genre
                            i=i+1
                        else:
                            movie.genre=str(movie.genre)+'/'+str(genre)
                            movie.titre=film['title']
                            movie.id=film['id']
                            movie.image=film['poster_path']
                            movie.note=film['vote_average']
                            movie.synopsis=film['overview']
                            if film['release_date']=='':
                                    pass
                            else:
                                movie.date_sortie=film['release_date']
                            if movie not in (films):
                                films.append(movie)
                                if Film.objects.filter(id=movie.id):
                                    pass
                                else:
                                    query = Film(id = movie.id , titre = movie.titre ,image= movie.image,synopsis=movie.synopsis,note=movie.note,genre=movie.genre,date_sortie=movie.date_sortie)
                                    query.save()
    paginator = Paginator(films, 18)

    page = request.GET.get('page')
    try:
        films = paginator.page(page)
    except PageNotAnInteger:
                # If page is not an integer, deliver first page.
        films = paginator.page(1)
    except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
        films = paginator.page(paginator.num_pages)

    context = {

        'object_list': films,
        'range':paginator.page_range,
        'genres':list_genre,
        'param': paramgenre

    }
    return render(request, 'blacksheep/film_search.html', context)

def serieAPI(nom):
    context=nom

def rechercheSerie(request):
    series=""
    query = request.GET.get('query')
    content = ''

    if not query:
        series = Serie.objects.all()
    else:
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

    if series=='':
        series=""

    paginator = Paginator(series, 10)
    page = request.GET.get('page')
    try:
        series = paginator.page(page)
    except PageNotAnInteger:
        series = paginator.page(1)
    except EmptyPage:
        series = paginator.page(paginator.num_pages)

    context = {'object_list': series,'range':paginator.page_range}


    return render(request, 'blacksheep/serie_search.html', context)
