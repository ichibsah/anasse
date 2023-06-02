from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from .views import (TestView, AppointmentView, IndexView, ContactView, AboutView, ServicesView, PortfolioView, PricingView, BlogView, CarouselView)

sitemaps = {
    "static": StaticViewSitemap,
}

app_name = "website"

urlpatterns = [
    # Add a comment for better readability
    # ------------------------------------
    # homepage view
    path('', IndexView.as_view(), name="home"),

    # Test view
    path("test.html", TestView.as_view(), name="testnew"),

    # appointment view
    path('appointment.html', AppointmentView.as_view(), name="appointment"),

    # contact view
    path('kontakt.html', ContactView.as_view(), name="contact"),

    # about view
    path('about.html', AboutView.as_view(), name="about"),

    # services view
    path('services.html', ServicesView.as_view(), name="services"),

    # portfolio view
    path('portfolio.html', PortfolioView.as_view(), name="portfolio"),

    # pricing view
    path('pricing.html', PricingView.as_view(), name="pricing"),

    # blog view
    path('stellenangebote.html', BlogView.as_view(), name="blog"),

    # carousel view
    path('carousel.html', CarouselView.as_view(), name="carousel"),

    # sitemap view
    path("sitemap.xml", sitemap,{"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]