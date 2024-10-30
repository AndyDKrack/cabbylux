# In vehicles/serializers.py
from rest_framework import serializers
from .models import Vehicle  # Adjust this import based on your Vehicle model's location

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_id', 'vehicle_make', 'vehicle_model', 'year_of_manufacture', 'vehicle_class_type', 
            'vehicle_number_plate', 'vehicle_color', 'vehicle_inspection_certificate', 'vehicle_image', 
            'owner_details', 'other_details', 'vehicle_insurance', 'vehicle_insurance_details', 
            'vehicle_specifications', 'additional_amenities', 'seating_capacity', 'accessibility_features', 
            'fuel_type', 'engine_capacity', 'event_suitability', 'chauffeur_or_driver_availability', 
            'vehicle_availability_status', 'vehicle_event_type', 'main_service', 'pick_up_point', 
            'drop_off_point', 'booking_history', 'pricing', 'deposit_required', 'payment_terms', 
            'feedback', 'reported_incidents', 'rating', 'gps_tracking_status', 'security_features', 
            'admin_authorization_status', 'admin_permission_chauffeurs_access', 'admin_notes'
        ]
