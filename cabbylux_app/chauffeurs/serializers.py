# In chauffeurs/serializers.py
from rest_framework import serializers
from .models import Chauffeur  # Adjust this import based on your Chauffeur model's location

class ChauffeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = [
            'chauffeur_id', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'residence', 
            'emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_residency', 
            'drivers_license_number', 'drivers_license_expiry_date', 'drivers_license', 
            'psv_license_number', 'psv_license', 'years_of_experience_certificate', 
            'defensive_driving_certificate', 'police_clearance_certificate', 'national_id_number', 
            'national_id', 'profile_picture', 'chauffeur_rating', 'completed_jobs', 
            'customer_reviews', 'reported_incidents', 'account_creation_date', 'account_status', 
            'last_active_date', 'availability', 'operating_area_preference', 'languages_spoken', 
            'gps_tracking_enabled', 'confidentiality_permission'
        ]
