from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<service_id>/', views.cart_add, name='cart_add'),
    path('remove/<service_id>/', views.cart_remove, name='cart_remove'),
]