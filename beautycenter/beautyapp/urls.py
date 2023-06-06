from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.service_list, name='service_list'),
    path('services/add/', views.add_service, name='add_service'),
    path('services/delete/<service_id>/', views.delete_service, name='delete_service'),
    path('services/<category_slug>/', views.service_list, name='service_list_by_category'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/delete/<category_id>/', views.delete_category, name='delete_category'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/delete/<client_id>/', views.delete_client, name='delete_client'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/delete/<doctor_id>/', views.delete_doctor, name='delete_doctor'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
