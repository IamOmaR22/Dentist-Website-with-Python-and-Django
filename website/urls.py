from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),
    path('pricing.html', views.pricing, name="pricing"),
    path('appointment.html', views.appointment, name="appointment"),
    path('booknow.html', views.booknow, name="booknow"),
]
