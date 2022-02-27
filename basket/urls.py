from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('basket/', views.view_basket, name='basket'),
    path('add_to_basket/<str:pk>', views.add_to_basket, name='add_to_basket'),
]
