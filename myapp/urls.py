from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
]