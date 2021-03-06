# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Serie(models.Model):
    firstAired = models.CharField(max_length=10)
    firstAired.default='2000-0-0'
    id = models.CharField(max_length=10)
    id.primary_key=True
    network = models.CharField(max_length=30)
    network.default=''
    overview = models.CharField(max_length=600)
    overview.default=''
    overview.null=True
    seriesName = models.CharField(max_length=64)
    seriesName.default=''
    status = models.CharField(max_length=20)
    status.default=''
    banner = models.CharField(max_length=20)
    banner.default=''


class Film(models.Model):
    titre = models.CharField(max_length=64)
    synopsis = models.TextField()
    synopsis.default=''
    note=models.CharField(max_length=4)
    note.default='0'
    image = models.CharField(max_length=64)
    image.null=True
    genre = models.CharField(max_length=64)
    genre.default=''
    genre.null=True
    date_sortie=models.DateField()
    date_sortie.null=True
    date_sortie.allow_future = True
    date_sortie.default='1900-01-01'



class Acteur(models.Model):
    titre = models.CharField(max_length=64)


class Genre(models.Model):
    name = models.CharField(max_length=64)
    name.default=''


class Pays(models.Model):
    titre = models.CharField(max_length=64)


class Producteur(models.Model):
    titre = models.CharField(max_length=64)


class Saison(models.Model):
    nbEpisode = models.CharField(max_length=64)


class Episode(models.Model):
    titre = models.CharField(max_length=64)
    synopsis = models.TextField
