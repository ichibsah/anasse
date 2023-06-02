from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from .models import CarouselImage
from django.urls import reverse
from django.views import generic
from django.contrib.sitemaps import Sitemap
from .mixin import GermanMixin


class TestView(GermanMixin, TemplateView):
    template_name = "test.html"
  

# Create your views here.
class IndexView(generic.ListView):
    template_name = "test.html"
    context_object_name = "latest_question_list"
    
def index(request):
    return render(request, 'index.html', customer_info)

def about(request):
    return render(request, 'about.html', customer_info)

def services(request):
    return render(request, 'services.html', customer_info)

def portfolio(request):
    return render(request, 'portfolio.html', customer_info)

def pricing(request):
    return render(request, 'pricing.html', customer_info)

def blog(request):
    return render(request, 'stellenangebote.html', customer_info)

def carousel(request):
    images = CarouselImage.objects.all()
    #a = {'carousel_images': carousel_images}
    #context = customer_info.values.__new__(a.values)
    #context = {'customer_info': customer_info, 'carousel_images': carousel_images}
    return render(request, 'carousel.html', {'carousel_images': images})
    #return render(request, 'carousel.html', context)

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['receiver@domain.com'] # to email
            
        )
        
        return render(request, 'kontakt.html', customer_info)
    
    else:
        return render(request, 'kontakt.html', customer_info)

def appointment(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['receiver@domain.com'] # to email
            
        )
        
        return render(request, 'appointment.html', {'message_name': message_name})
    
    else:
        return render(request, 'home.html', customer_info)