from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact_info/',views.contactinfo,name='contact_info'),
    path('contact/',views.contact,name='contact'),
    
]