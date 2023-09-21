# app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_class/', views.add_class, name='add_class'),
    # Add more URLs as needed
]
