from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("services", views.services, name='services'),
    path("product", views.product, name='product'),
    path("about", views.about, name='about'), 
    path("contact", views.contact, name='contact'), 
]