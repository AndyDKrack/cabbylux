from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year_of_manufacture = models.IntegerField()
    vehicle_class_type = models.CharField(max_length=20, choices=[('SUV', 'SUV'), ('limousine', 'Limousine'), ('sedan', 'Sedan'), ('sports car', 'Sports Car'), ('luxury bus', 'Luxury Bus')])
    number_plate = models.CharField(max_length=15, unique=True)
    colour = models.CharField(max_length=50)
    inspection_certificate = models.FileField(upload_to='inspection_certificates/')
    vehicle_image = models.ImageField(upload_to='vehicle_images/')
    owner_first_name = models.CharField(max_length=50)
    owner_last_name = models.CharField(max_length=50)
    owner_phone_number = models.CharField(max_length=15)
    owner_email = models.EmailField()
    privately_owned = models.BooleanField(default=True)  # True if privately owned, False if leased
    vehicle_insurance = models.FileField(upload_to='vehicle_insurances/')
    insurance_policy_number = models.CharField(max_length=50)
    insurance_provider = models.CharField(max_length=100)
    insurance_expiry_date = models.DateField()
    specifications = models.TextField(null=True, blank=True)  # Detailed specs
    additional_amenities = models.TextField(null=True, blank=True)  # Amenities like Wi-Fi, etc.
    seating_capacity = models.IntegerField()
    accessibility_features = models.TextField(null=True, blank=True)
    fuel_type = models.CharField(max_length=20)
    engine_capacity = models.FloatField()
    event_suitability = models.CharField(max_length=100)  # e.g., weddings, corporate events
    chauffeur_or_driver_available = models.BooleanField(default=True)
    availability_status = models.CharField(max_length=20, choices=[('available', 'Available'), ('booked', 'Booked'), ('in service', 'In Service')])
    main_service = models.JSONField(default=dict)  # e.g., {"type": "location-destination"}
    pick_up_point = models.CharField(max_length=100)
    drop_off_point = models.CharField(max_length=100)
    booking_history = models.JSONField(default=list)  # e.g., [{...}, {...}]
    pricing = models.JSONField(default=dict)  # e.g., {"hourly": 20, "daily": 100}
    deposit_required = models.BooleanField(default=False)
    payment_terms = models.CharField(max_length=100)
    feedback = models.TextField(null=True, blank=True)
    reported_incidents = models.TextField(null=True, blank=True)
    rating = models.FloatField(default=0)  # Average rating
    gps_tracking_status = models.BooleanField(default=True)
    security_features = models.TextField(null=True, blank=True)
    admin_authorization_status = models.CharField(max_length=20, choices=[('approved', 'Approved'), ('pending', 'Pending Approval'), ('denied', 'Denied')])
    admin_permission_for_chauffeurs = models.BooleanField(default=False)
    admin_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.number_plate})"
