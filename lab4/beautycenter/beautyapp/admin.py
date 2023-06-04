from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Service, ServiceAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['service']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(Profile)