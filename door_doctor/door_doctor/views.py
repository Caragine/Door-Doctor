from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class AboutUs(TemplateView):
    template_name = 'about_us.html'

class Gallery(TemplateView):
    template_name = 'gallery.html'

class Services(TemplateView):
    template_name = 'servicerepair.html'

class FAQ(TemplateView):
    template_name = 'faq.html'

class contact(TemplateView):
    template_name = 'contact.html'