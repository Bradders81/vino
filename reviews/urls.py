from django.urls import path
from .import views


urlpatterns = [
    path('reviews/', views.user_reviews, name='reviews'),

]