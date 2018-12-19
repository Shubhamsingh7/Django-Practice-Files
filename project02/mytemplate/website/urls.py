from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePageview.as_view(),name="home"),
    path('about/',views.aboutUsView.as_view(),name="about"),
    path('contact/',views.contactusView.as_view(),name="contact"),
    path('service/',views.serviceview.as_view(),name="service"),

]
