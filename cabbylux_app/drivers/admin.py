# users/admin.py
from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'license_number', 'phone_number', 'status')
    search_fields = ('name', 'license_number')
    list_filter = ('status',)
