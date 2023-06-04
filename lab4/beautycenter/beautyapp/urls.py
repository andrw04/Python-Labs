from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('service_list/', views.service_list, name='service_list'),
    path('service_list/<category_slug>/', views.service_list, name='service_list_by_category'),
    path('service_detail/<id>/<slug>/', views.service_detail, name='service_detail'),
    path('orders/create/', views.order_create, name='order_create'),
]

