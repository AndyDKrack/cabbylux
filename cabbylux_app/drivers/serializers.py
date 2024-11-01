# In drivers/serializers.py
from rest_framework import serializers
from .models import Driver  # Adjust this import based on your Driver model's location

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'driver_id', 'name', 'email', 'phone_number', 'current_residency', 
            'emergency_contact', 'driver_license_number', 'driver_license_expiry_date',
            'driver_license', 'psv_license_badge_number', 'psv_license_badge', 'national_id_number', 
            'national_id', 'profile_picture', 'certificate_of_police_clearance', 
            'certificate_of_police_clearance_number', 'vehicle_details', 'vehicle_registration_number', 
            'vehicle_color', 'vehicle_insurance_details', 'vehicle_insurance', 'driver_rating', 
            'number_of_completed_rides', 'customer_review', 'incident_report', 'account_status', 
            'date_of_account_creation', 'last_active_date', 'login_history', 'payment_methods', 
            'earning_history', 'app_commission', 'trips_made'
        ]
