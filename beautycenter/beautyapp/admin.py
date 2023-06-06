from django.contrib import admin
from .models import Service, Category, Client, Doctor


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'slug', 'image', 'description', 'price', 'available', 'created', 'updated')
    list_filter = ('name', 'price')


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'image', 'category')
    list_filter = ('first_name', 'last_name')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address', 'mobile')
    list_filer = ('first_name', 'last_name')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category)
admin.site.register(Client, ClientAdmin)
admin.site.register(Doctor, DoctorAdmin)
