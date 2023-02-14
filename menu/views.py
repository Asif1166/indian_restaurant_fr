from django.shortcuts import render
from .models import *
from itertools import chain
from home.models import Contact

# Create your views here.
def menu(request):
    Entrées = Nos_Entrées.objects.all()
    Nans = Nos_Nans.objects.all()
    Nans2 = Nos_Paratha.objects.all()
    Nans3 = Nos_Biriyani.objects.all()
    Nans4 = Nos_Poulets.objects.all()
    Nans5 = Nos_Plats.objects.all()
    Nans6 = MENU.objects.all()
    Nans7 = Nos_légumes.objects.all()
    Nans8 = Nos_Crustacés.objects.all()
    Nans9 = Nos_Frites.objects.all()
    Nans10 = Nos_Viandes.objects.all()
    Nans11 = Nos_sauces.objects.all()
    Nans12 = Nos_desserts.objects.all()
    Nans14 = Nos_Boisson.objects.all()
    Nans15 = Nos_Cocktails.objects.all()
    Nans16 = Nos_Lassis.objects.all()
    Nans17 = Nos_Chaudes.objects.all()
    Nans18 = Café.objects.all()
    contacts = Contact.objects.all()
    
    data = list(chain(Entrées, Nans, Nans2,Nans3,Nans4,Nans5,Nans6,Nans7,Nans8,Nans9,Nans10,Nans11,Nans12,Nans14,Nans15,Nans16,Nans17,Nans18,))
    context = {
        
        'data':data,
        'contacts':contacts,
        
    }
    return render(request, 'pages/menu.html',context)