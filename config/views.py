from django.shortcuts import render
from django.core.mail import send_mail
from .models import CarouselImage

customer_info = {
    "cName": "A N A S S E",
    "cSlogan": "Hotelservice & Dienstleistungen",
    "cInH": "InH. Anasse Boukari",
    "cAddr": "Koblenzer straße 31",
    "cPLZ": "60327",
    "cCity": "Frankfurt am Main",
    "cState": "Hessen",
    "cTel": "+49 176 638 993 63",
    "cOpnMn": "Mon-DO: 09:00 bis 18:00 Uhr",
    "cOpnFr": "FR: 09:00 bis 15:00 Uhr",
    "message_name": "message_name",
    "cWebsite": "https://anasse.de",
    "cEmail": "info@anasse.de",
    "cQuestions": "Have a Questions?",
    "cOpenHrs": "Geschäftszeiten",
    "cOpenDays": "Öffnungstage:",
    "cEmergency": "Für Notfälle",
    "cVaccation": "Ferien",
    "cWorks": "Die Art von Arbeiten, die wir ausführen",
    "cSubheading": "Sauber Räume, glückliche Gesichter",
    "cFriendly": "Wir verwenden umweltfreundliche Reinigungsprodukte für Kunden, die ökologische Reinigungslösungen bevorzugen.",
    "cMission": "Unsere Mission ist es, das vertrauenswürdigste und zuverlässigste Reinigungsunternehmen in der Region zu werden. Wir werden dies erreichen, indem wir außergewöhnliche Reinigungsdienste anbieten, umweltfreundliche Reinigungsprodukte verwenden und wettbewerbsfähige Preise anbieten.",
    
        
}
# Create your views here.
def home(request):
    return render(request, 'home.html', customer_info)

def about(request):
    return render(request, 'about.html', customer_info)

def services(request):
    return render(request, 'services.html', customer_info)

def portfolio(request):
    return render(request, 'portfolio.html', customer_info)

def pricing(request):
    return render(request, 'pricing.html', customer_info)

def blog(request):
    return render(request, 'blog.html', customer_info)

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
        
        return render(request, 'contact.html', customer_info)
    
    else:
        return render(request, 'contact.html', customer_info)

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