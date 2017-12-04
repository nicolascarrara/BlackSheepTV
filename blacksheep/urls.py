from django.conf.urls import url, include
from .views import serieAPI,rechercheFilm, rechercheSerie,accueil, FilmListView, SerieListView, FilmDetailView, SerieDetailView, SaisonDetailView, EpisodeDetailView,loginAPI,search



app_name = 'blacksheep'
urlpatterns = [
    url(r'^$', accueil, name='accueil'),
    url(r'^loginAPI/', loginAPI, name='loginAPI'),
    url(r'^search/', search, name='search'),
    url(r'^film$', FilmListView.as_view(), name='film-list'),
    url(r'^film/search', rechercheFilm, name='film-search'),
    url(r'^detailFilm/(?P<pk>\d+)$', FilmDetailView.as_view(), name='film-detail'),
    url(r'^serie/$', SerieListView.as_view(), name='serie-list'),
    url(r'^serie/search/$', rechercheSerie, name='serie-search'),
    url(r'^serie/search/api/.*/', serieAPI, name='serieAPI'),
    url(r'^detailSerie/(?P<pk>\d+)$',
        SerieDetailView.as_view(), name='serie-detail'),
    url(r'^detailSerie/(?P<pk>\d+)/saison/(?P<pk2>\d+)$',
        SaisonDetailView.as_view(), name='serie-saison-detail'),
    url(r'^detailSerie/(?P<pk>\d+)/saison/(?P<pk2>\d+)/episode/(?P<pk3>\d+)$',
        EpisodeDetailView.as_view(), name='serie-saison-episode-detail'),

]
