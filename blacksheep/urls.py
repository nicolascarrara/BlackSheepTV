from django.conf.urls import url, include
from . import views
<<<<<<< HEAD
from .views import accueil, test, FilmListView, SerieListView, FilmDetailView, SerieDetailView
=======
from .views import accueil, FilmListView, SerieListView, FilmDetailView, SerieDetailView, SaisonDetailView, EpisodeDetailView
>>>>>>> b46273f5e8aa9979eedd46f51404df9b8858222f


app_name = 'blacksheep'
urlpatterns = [
    url(r'^$', accueil, name='accueil'),
    url(r'^test/', test, name='test'),
    url(r'^film$', FilmListView.as_view(), name='film-list'),
    url(r'^detailFilm/(?P<pk>\d+)$', FilmDetailView.as_view(), name='film-detail'),
    url(r'^serie$', SerieListView.as_view(), name='serie-list'),
    url(r'^detailSerie/(?P<pk>\d+)$',
        SerieDetailView.as_view(), name='serie-detail'),
    url(r'^detailSerie/(?P<pk>\d+)/saison/(?P<pk2>\d+)$',
        SaisonDetailView.as_view(), name='serie-saison-detail'),
    url(r'^detailSerie/(?P<pk>\d+)/saison/(?P<pk2>\d+)/episode/(?P<pk3>\d+)$',
        EpisodeDetailView.as_view(), name='serie-saison-episode-detail'),

]
