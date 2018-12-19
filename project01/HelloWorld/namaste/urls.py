
from django.urls import path
from . import views


urlpatterns = [

    path("/namaste",views.namasteView,name="index")
]
