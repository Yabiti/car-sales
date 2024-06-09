from django.urls import path

from . import views
urlpatterns = [
    path("home/", views.home, name="home"),
    path("insertuser", views.insertuser, name="insertuser"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact")
]