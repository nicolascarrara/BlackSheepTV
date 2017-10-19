from django.conf.urls import url, include
from . import views
from .views import accueil


app_name = 'blacksheep'
urlpatterns = [
    url(r'^$', accueil, name='accueil'),

]
