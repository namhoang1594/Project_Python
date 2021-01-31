from django.conf.urls.static import static
from django.urls import path

from Productdb import settings
from Productweb import views

urlpatterns = [
    path("", views.home, name="home"),
    path("details", views.details, name = "details"),

]
