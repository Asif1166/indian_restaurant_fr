from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('specials/', views.specials, name='specials'),
    path('gallery/', views.gallery, name='gallery'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('chefs/', views.chefs, name='chefs'),
    
]