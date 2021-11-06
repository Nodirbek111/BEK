from django.views.generic import TemplateView

class Jaxa(TemplateView):
    template_name="index.html"

class Jaxan(TemplateView):
    template_name="about.html"

class kurslar(TemplateView):
    template_name='courses.html'
    
class Mars(TemplateView):
    template_name='portfolio.html'
    
class bek(TemplateView):
     template_name='pricing.html'
    
class auff(TemplateView):
      template_name='contact.html'  