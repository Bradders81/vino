from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('product-info/<str:pk>/', views.product_info, name='product-info'),
    path('edit_product/<str:pk>/', views.edit_product, name='edit_product'),
]
