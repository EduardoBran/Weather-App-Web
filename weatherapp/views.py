import datetime

import requests
from django.shortcuts import redirect, render


def homeView(request):
    api_call_site = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
    
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Niteroi'
        
    if city == None or city == "":
        city = 'Niteroi'  # enviar mensagem de 'voce precisa digitar um nome de cidade'
    
    appid = '135b2cbe9493a774efcf3e7177bcd6bd'    
    
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    PARAMS = {
        'q': city,
        'appid': appid,
        'units': 'metric',
        'lang': 'pt_br'
    }
    
    r = requests.get(url=URL, params=PARAMS)
    
    if r.status_code == 404:
        return redirect('home') # enviar mensagem de 'cidade nao existe'
    
    res = r.json()
    
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    
    day = datetime.date.today()
    
    humidity = res['main']['humidity']
    tempMin = res['main']['temp_min']
    tempMax = res['main']['temp_max']
    country = res['sys']['country']
    
    context = {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
        'humidity': humidity,
        'country': country,
        'tempMin': tempMin,
        'tempMax': tempMax,
    }
    return render(request, 'weatherapp/home.html', context)
