from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import cmdr

class homePageView(ListView):
    model=cmdr
    template_name='home.html'

class aboutUsView(ListView):
    model=cmdr
    template_name='aboutus.html'


class contactusView(ListView):
    model=cmdr
    template_name='contactus.html'


class serviceview(ListView):
    model=cmdr
    template_name="services.html"

# Create your views here.
