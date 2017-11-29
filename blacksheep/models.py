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
    seriesName = models.CharField(max_length=64)
    seriesName.default=''
    status = models.CharField(max_length=20)
    status.default=''


class Film(models.Model):
    titre = models.CharField(max_length=64)
    """ artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return'{self.titre}'.format(self=self)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('musiques:morceau-detail', args=[str(self.id)])"""


class Acteur(models.Model):
    titre = models.CharField(max_length=64)


class Genre(models.Model):
    titre = models.CharField(max_length=64)


class Pays(models.Model):
    titre = models.CharField(max_length=64)


class Producteur(models.Model):
    titre = models.CharField(max_length=64)


class Saison(models.Model):
    nbEpisode = models.CharField(max_length=64)


class Episode(models.Model):
    titre = models.CharField(max_length=64)
    synopsis = models.TextField
