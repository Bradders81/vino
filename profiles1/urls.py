from django.urls import path
from .import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('order_history/<str:order_number>/',
         views.order_history, name='order_history'),
    path('delete_user/<str:username>', views.delete_user, name='delete_user'),

]

