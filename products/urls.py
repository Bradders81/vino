from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products, name='products'),
    path('product-info/<str:pk>/', views.product_info, name='product-info'),
    path('add/', views.add_product, name='add_product'),
]
