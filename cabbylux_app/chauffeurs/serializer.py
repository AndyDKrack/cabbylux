# In chauffeurs/serializers.py
from rest_framework import serializers
from .models import Chauffeur  # Adjust this import based on your Chauffeur model's location

class ChauffeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = [
            'chauffeur_id', 'name', 'date_of_birth', 'contact_information', 'residence', 
            'emergency_contact_name', 'emergency_contact_phone_number', 'emergency_contact_residency', 
            'driver_license_number', 'driver_license_expiry_date', 'driver_license', 
            'psv_license_badge_number', 'psv_license_badge', 'years_of_experience_certification', 
            'defensive_driving_certificate', 'certificate_of_police_clearance', 'national_id_number', 
            'national_id', 'profile_picture', 'chauffeur_rating', 'number_of_completed_jobs', 
            'customer_reviews', 'reported_incidents', 'account_creation_date', 'account_status', 
            'last_active_date', 'availability', 'operating_area_preferences', 'languages_spoken', 
            'real_time_gps_tracking', 'legal_permission_confidentiality'
        ]
