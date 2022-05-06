from django.urls import path
from .import views


urlpatterns = [
    path('reviews/', views.user_reviews, name='reviews'),
    path('display_wine_reviews/<str:wine_id>/',
         views.display_wine_reviews, name='display_wine_reviews'),
]