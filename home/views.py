from django.shortcuts import render
from .models import Testimonial, Gallery, Contact, About_us, Event, Chef, Social_link
from django.core.mail import send_mail

# Create your views here.
def home(request):
    testimonials = Testimonial.objects.all()
    contacts= Contact.objects.all()
    social = Social_link.objects.all()
    context= {
        'testimonials':testimonials,
        'contacts':contacts,
        'social':social
    }
    return render(request, 'home.html',context)

def about(request):
    about = About_us.objects.all()
    contacts= Contact.objects.all()
    
    context = {
        'about':about,
        'contacts':contacts,
    }
    return render(request, 'pages/about.html', context)



def specials(request):
    return render(request, 'pages/specials.html',)

def gallery(request):
    contacts= Contact.objects.all()
    gallery = Gallery.objects.all()
    context = {
        'gallery':gallery,
        'contacts':contacts,
    }
    return render(request, 'pages/gallery.html', context)

def reservation(request):
    return render(request, 'pages/reservation.html',)

def contact(request):
    contacts= Contact.objects.all()
    context = {
        'contacts':contacts,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New Message: {}
        
        from: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['pizzahelen2023@gmail.com'])
        
        
    return render(request, 'pages/contact.html', context)

def events(request):
    events = Event.objects.all()
    contacts= Contact.objects.all()
    
    context = {
        'events':events,
        'contacts':contacts
    }
    return render(request, 'pages/events.html', context)

def chefs(request):
    
    chef = Chef.objects.all()
    contacts= Contact.objects.all()
    
    context = {
        'chef':chef,
        'contacts':contacts,
    }
    return render(request, 'pages/chefs.html',context)
