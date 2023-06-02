from django.urls import path
from django.contrib.sitemaps.views import sitemap
#from . import views
from .sitemaps import StaticViewSitemap
from .views import (
    TestView, appointment
)


sitemaps = {
    "static": StaticViewSitemap,
}

app_name = "website"
urlpatterns = [
    #path("test", views.IndexView.as_view(), name="test"),
    path("test.html", TestView.as_view(), name="testnew"),
    path('', views.index, name="home"),
    #path('index.html', views.home, name="index"),
    #path('home.html', views.home, name="index"),
    path('appointment.html', appointment, name="appointment"),
    path('kontakt.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('services.html', views.services, name="services"),
    path('portfolio.html', views.portfolio, name="portfolio"),
    path('pricing.html', views.pricing, name="pricing"),
    path('stellenangebote.html', views.blog, name="blog"),
    path('carousel.html', views.carousel, name="carousel"),

    path("sitemap.xml", sitemap,{"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),

]
