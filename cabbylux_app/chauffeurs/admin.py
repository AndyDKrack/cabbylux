# users/admin.py
from django.contrib import admin
from .models import Chauffeur

@admin.register(Chauffeur)
class ChauffeurAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'experience_level', 'phone_number', 'vip_approved')
    search_fields = ('name', 'experience_level')
    list_filter = ('vip_approved', 'experience_level')

