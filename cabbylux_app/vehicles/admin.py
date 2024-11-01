# users/admin.py
from django.contrib import admin
from .models import Vehicle, Driver

class DriverInline(admin.TabularInline):  # Inline for associated drivers
    model = Driver
    extra = 1

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'year', 'vip')
    search_fields = ('make', 'model')
    list_filter = ('vip',)
    inlines = [DriverInline]

