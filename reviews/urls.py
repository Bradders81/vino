from django.urls import path
from .import views


urlpatterns = [
    path('reviews/', views.user_reviews, name='reviews'),
    path('product_reviews/<str:wine_id>/',
         views.product_reviews, name='product_reviews'),
    path('review_details/<str:review_id>/',
         views.review_details, name='review_details'),
]