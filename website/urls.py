from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}

app_name = "website"
urlpatterns = [
    path("test", views.IndexView.as_view(), name="test"),
    path('', views.home, name="home"),
    path('index.html', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path('appointment.html', views.appointment, name="appointment"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('services.html', views.services, name="services"),
    path('portfolio.html', views.portfolio, name="portfolio"),
    path('pricing.html', views.pricing, name="pricing"),
    path('blog.html', views.blog, name="blog"),
    path('carousel.html', views.carousel, name="carousel"),

    path("sitemap.xml", sitemap,{"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),

]
