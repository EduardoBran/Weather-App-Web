from django.shortcuts import render


def homeView(request):
    url = 'http://api.openweathermap.org/data/2.5/forecast?d=524901&appid=135b2cbe9493a774efcf3e7177bcd6bd'
    APPID = '135b2cbe9493a774efcf3e7177bcd6bd'    
    
    context = {}
    return render(request, 'weatherapp/home.html', context)
