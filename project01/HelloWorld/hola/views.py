from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def holaHomePageView(request):
    return HttpResponse("Hola Means Hello in Spanish")
