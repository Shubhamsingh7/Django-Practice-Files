from django.views.generic import TemplateView


class homePageview(TemplateView):
    template_name='home.html'


class aboutUsView(TemplateView):
    template_name='aboutus.html'


class contactusView(TemplateView):
    template_name='contactus.html'


class serviceview(TemplateView):
    template_name="services.html"
