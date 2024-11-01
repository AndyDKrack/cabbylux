# users/admin.py
from django.contrib import admin
from .models import Vehicle
from drivers.models import Driver
from chauffeurs.models import Chauffeur

class DriverInline(admin.TabularInline):
    model = Driver
    extra = 1

class ChauffeurInline(admin.TabularInline):
    model = Chauffeur
    extra = 1

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'make', 'model', 'year_of_manufacture', 'vehicle_image')
    search_fields = ('make', 'model')
    list_filter = ('vehicle_class_type', 'availability_status')
    inlines = [DriverInline, ChauffeurInline]


