# In users/serializers.py
from rest_framework import serializers
from .models import User  # Adjust this import based on your User model's location

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id', 'first_name', 'last_name', 'email', 'phone_number', 'profile_picture', 'residence_location',
            'work_location', 'add_location', 'number_of_trips_taken'
        ]
