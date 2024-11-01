# In vehicles/serializers.py
from rest_framework import serializers
from .models import Vehicle  # Adjust this import based on your Vehicle model's location

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_id', 'make', 'model', 'year_of_manufacture', 'vehicle_class_type', 
            'number_plate', 'colour', 'inspection_certificate', 'vehicle_image', 
            'owner_first_name', 'owner_last_name', 'owner_phone_number', 'owner_email', 'privately_owned', 'vehicle_insurance', 'insurance_policy_number', 'insurance_provider', 'insurance_expiry_date',  
            'specifications', 'additional_amenities', 'seating_capacity', 'accessibility_features', 
            'fuel_type', 'engine_capacity', 'event_suitability', 'chauffeur_or_driver_available', 
            'availability_status', 'main_service', 'pick_up_point', 
            'drop_off_point', 'booking_history', 'pricing', 'deposit_required', 'payment_terms', 
            'feedback', 'reported_incidents', 'rating', 'gps_tracking_status', 'security_features', 
            'admin_authorization_status', 'admin_permission_for_chauffeurs', 'admin_notes'
        ]
