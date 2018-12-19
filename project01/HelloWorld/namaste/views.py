from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def namasteView(request):
    return HttpResponse("Namaste Means Hello in Hindi")
