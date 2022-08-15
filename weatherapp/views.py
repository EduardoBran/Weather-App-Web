import datetime

import requests
from django.shortcuts import render


def homeView(request):
    api_call_site = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Niteroi'
    
    appid = '135b2cbe9493a774efcf3e7177bcd6bd'    
    
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    PARAMS = {
        'q': city,
        'appid': appid,
        'units': 'metric'
    }
    
    r = requests.get(url=URL, params=PARAMS)
    
    res = r.json()
    
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    
    day = datetime.date.today()
    
    context = {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
    }
    return render(request, 'weatherapp/home.html', context)
