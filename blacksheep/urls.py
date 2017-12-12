from django.conf.urls import url, include
from .views import discoverAPI,FilmList, TrailerFilmAPI, rechercheFilm, rechercheSerie,accueil, SerieList, FilmDetailView, SerieDetailView, SaisonDetailAPI, EpisodeDetailAPI,loginAPI


app_name = 'blacksheep'
urlpatterns = [
    url(r'^$', accueil, name='accueil'),
    url(r'^loginAPI/', loginAPI, name='loginAPI'),
    url(r'^film/discoverAPI',discoverAPI, name='discoverAPI'),
    url(r'^film$', FilmList, name='film-list'),
    url(r'^film/film_trailer', TrailerFilmAPI, name='film-trailer'),
    url(r'^film/search', rechercheFilm, name='film-search'),
    url(r'^detailFilm/(?P<pk>\d+)$', FilmDetailView.as_view(), name='film-detail'),
    url(r'^serie/$', SerieList, name='serie-list'),
    url(r'^serie/search/$', rechercheSerie, name='serie-search'),
    url(r'^detailSerie/(?P<pk>\d+)$',
        SerieDetailView.as_view(), name='serie-detail'),
    url(r'^detailSerie/saison/',SaisonDetailAPI, name='serie-saison-detail'),
    url(r'^detailSerie/episode/',EpisodeDetailAPI, name='serie-saison-episode-detail'),

]
