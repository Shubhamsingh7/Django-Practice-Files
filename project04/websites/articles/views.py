from django.views.generic import ListView

from  .models import Article
# Create your views here.


class Homeview(ListView):
    model=Article
    my_template='home.html'
