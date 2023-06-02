from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from .models import CarouselImage
from django.urls import reverse
from django.views import generic
from django.contrib.sitemaps import Sitemap
from .mixin import GermanMixin


class AppointmentView(GermanMixin, TemplateView):
    template_name = "appointment.html"
    

class TestView(GermanMixin, TemplateView):
    template_name = "test.html"
  

class IndexView(GermanMixin, TemplateView):
    template_name = "index.html"



class AboutView(GermanMixin, TemplateView):
    template_name = "about.html"
  

class ServicesView(GermanMixin, TemplateView):
    template_name = "services.html"
  

class PortfolioView(GermanMixin, TemplateView):
    template_name = "portfolio.html"
  

class PricingView(GermanMixin, TemplateView):
    template_name = "pricing.html"
  

class BlogView(GermanMixin, TemplateView):
    template_name = "stellenangebote.html"


class CarouselView(GermanMixin, TemplateView):
    template_name = "carousel.html"


class ContactView(GermanMixin, TemplateView):
    template_name = "kontakt.html"

    def post(self, request, *args, **kwargs):
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
   