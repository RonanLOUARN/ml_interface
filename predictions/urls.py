from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.prediction_index),
    path('new/', views.prediction_new, name='prediction_new'),
]
