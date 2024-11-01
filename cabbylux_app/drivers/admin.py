# users/admin.py
from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('driver_id', 'first_name', 'last_name', 'drivers_license_number', 'phone_number', 'driver_rating')
    search_fields = ('first_name', 'drivers_license_number')
    list_filter = ('first_name', 'last_name', 'driver_rating')
