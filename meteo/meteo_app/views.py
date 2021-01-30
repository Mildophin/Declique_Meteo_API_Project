from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    cities = City.objects.all()  # J'indique que les villes à afficher sont celles listées dans la base de données

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=fr&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()  # fonctionne seulement si un formulaire est envoyé, puis ajoute les datas récupérées et valide le tout si tout est bon

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()  # je demande à l'API les datas et elle convertit les données JSON en python

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)  # ajoute les datas de cette ville dans la base de données

    context = {'weather_data': weather_data, 'form': form}  # renvoie la page index.html

    return render(request, 'meteo_app/index.html', context)
