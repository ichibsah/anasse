class GermanMixin:
    cinfo = {
    "cName": "A N A S S E",
    "cSlogan": "Hotel Service & Services",
    "cInH": "Inh. Anasse Boukari",
    "cAddr": "Koblenzer Strasse 31",
    "cPLZ": "60327",
    "cCity": "Frankfurt am Main",
    "cState": "Hesse",
    "cTel": "+49 176 638 993 63",
    "cOpnMn": "Mon-Thu: 09:00 am to 06:00 pm",
    "cOpnFr": "Fri: 09:00 am to 03:00 pm",
    "message_name": "message_name",
    "cWebsite": "https://anasse.de",
    "cEmail": "info@anasse.de",
    "cQuestions": "Have any questions?",
    "cOpenHrs": "Business Hours",
    "cOpenDays": "Opening Days:",
    "cEmergency": "For Emergencies",
    "cVacation": "Vacation",
    "cWorks": "The type of work we do",
    "cSubheading": "Clean rooms, happy faces",
    "cFriendly": "We use eco-friendly cleaning products for customers who prefer ecological cleaning solutions.",
    "cMission": "Our mission is to become the most trusted and reliable cleaning company in the region. We will achieve this by providing exceptional cleaning services, using environmentally friendly cleaning products, and offering competitive prices.",
    "cQLinks": "Quick Links",
    "cNHome": "Home",
    "cNAbout": "About Us",
    "cNServices": "Services",
    "cNBlog": "Job Opportunities",
    "cNContact": "Contact",
    "cSOffice": "Building Cleaning",
    "cSOfficeSl": "We provide competent staff for your needs, whether it's for basic cleaning or daily maintenance. Maintenance cleaning, office cleaning, wellness and spa areas, glass cleaning, carpet cleaning / shampooing.",
    "cSKitchen": "Stewarding",
    "cSKitchenSl": "The kitchen requires constant monitoring in terms of quality and cost. Relief in staff disposition allows you to focus on YOUR core business. We are your contact in this area and stand out through years of experience and expertise.",
    "cSReception": "Reception",
    "cSReceptionSl": "A friendly and competent reception is the key to a hospitable house; here we offer you suitable personnel to ensure your standard. Talk to us.",
    "cSService": "Service",
    "cSServiceSl": "Service is our passion! Whether in restaurant service, banquet, or gala, we offer you the appropriate cooperation opportunities.",
    "cSHousekeep": "Housekeeping",
    "cSHousekeepSl": "Anasse Hotelservice stands for top-class cleaning work! Room cleaning, provision of housekeeping, minibar service, cover service / turndown, bed and laundry services, mattress cleaning, maintenance of public areas and outdoor facilities, conference service, foreman for training, general personnel service. In general, we offer you the following services, here is an overview of our services:",
    "cSCatering": "Catering",
    "cSCateringSl": "Banquet and conference service, personnel services, reception service, mail and messenger services, entrance mat service, janitorial services."
}

    
    my_data1 = {
        'product': 'Laptop',
        'brand': 'Lenovo',
        'model': 'Thinkpad Carbon X1'
    }
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cinfo'] = self.cinfo
        context['my_data1'] = self.my_data1
        return context