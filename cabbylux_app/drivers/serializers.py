# In drivers/serializers.py
from rest_framework import serializers
from .models import Driver  # Adjust this import based on your Driver model's location

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'driver_id', 'first_name', 'last_name', 'email', 'phone_number', 'current_residency', 
            'emergency_contact_name', 'emergency_contact_phone', 'drivers_license_number', 'drivers_license_expiry_date',
            'drivers_license', 'psv_license_number', 'psv_license', 'national_id_number', 
            'national_id', 'profile_picture', 'police_clearance_certificate', 
            'police_clearance_number', 'vehicle_details', 'vehicle_registration_number', 
            'vehicle_colour', 'vehicle_insurance_policy_number', 'vehicle_insurance_expiry_date', 'vehicle_insurance', 'driver_rating', 
            'completed_rides', 'customer_review', 'incident_report', 'account_status', 
            'date_of_account_creation', 'last_active_date', 'login_history', 'payment_methods', 
            'earning_history', 'app_commission', 'trips_made'
        ]
