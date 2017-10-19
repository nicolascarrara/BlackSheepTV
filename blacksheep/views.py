from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from BlackSheepTV import settings
import requests

# Create your views here.


def accueil(request):
    return render(request, 'blacksheep/accueil.html')


def test(request):
    parameters = {'apikey': "C9D85668BADC5AD4",
                  'userkey': "04565F600F78B2C0", 'username': "nicolascarrara"}
    response = requests.post(
        "https://api.thetvdb.com/login", params=parameters)
    data = response.json()
    """
    decoders = [
        codecs.JSONCodec()
    ]
    client = coreapi.Client(decoders=decoders)
    schema = client.get('https://api.thetvdb.com/login')

    action = ['api-token-auth', 'obtain-token']
    params = {'apikey': "C9D85668BADC5AD4",
              'userkey': "04565F600F78B2C0", 'username': "nicolascarrara"}
    result = client.action(schema, action, params)

    auth = coreapi.auth.TokenAuthentication(
        scheme='JWT',
        token=result['token']
    )
    client = coreapi.Client(auth=auth)"""
    return render(request, data, 'blacksheep/test.html')
