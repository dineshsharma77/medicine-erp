from . import views
from django.urls import path

urlpatterns = [
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('contact/save', views.save_contact, name='save_contact'),


]
