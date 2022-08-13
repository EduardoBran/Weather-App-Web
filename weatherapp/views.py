from django.shortcuts import render


def homeView(request):
    context = {}
    return render(request, 'weatherapp/home.html', context)
