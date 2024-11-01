# users/admin.py
from django.contrib import admin
from .models import Chauffeur

@admin.register(Chauffeur)
class ChauffeurAdmin(admin.ModelAdmin):
    list_display = ('chauffeur_id', 'first_name', 'last_name', 'phone_number', 'chauffeur_rating')
    search_fields = ('first_name', 'last_name', 'years_of_experience_certificate')
    list_filter = ('first_name', 'chauffeur_rating')

