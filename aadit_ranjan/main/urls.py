from . import views
from django.urls import path
from django.conf.urls import static


urlpatterns = [
    path('', views.renderHomePage), # homepage renders by .
       
] 
