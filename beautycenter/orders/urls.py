from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('', views.order_list, name='order_list'),
    path('delete/<order_id>/', views.delete_order, name='delete_order'),
]