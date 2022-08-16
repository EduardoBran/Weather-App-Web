import datetime

import requests
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContatoForm


def homeView(request):
    api_call_site = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
    
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Rio de Janeiro'
        
    if city == None or city == "":
        city = 'Rio de Janeiro'
    
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
        messages.add_message(
            request,
            messages.ERROR,
            'Cidade não encontrada.'
        )
        return redirect('home')
    
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


def sobreView(request):
    if str(request.method) == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            #chamando método de envio de email
            form.send_email()
            messages.success(request, 'Email enviado com sucesso.')
            form = ContatoForm()
        else:
            messages.error(request, 'Email NÃO FOI enviado com sucesso.')
    else:
        form = ContatoForm()

    context = {
        'form':form
    }
    return render(request, 'weatherapp/sobre.html', context)



def projetosView(request):
    return render(request, 'weatherapp/projetos.html')
