from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('sobre/', views.sobreView, name='sobre'),
]
