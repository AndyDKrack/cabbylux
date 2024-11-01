from django.db import models
from vehicles.models import Vehicle 

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    current_residency = models.CharField(max_length=100)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    drivers_license_number = models.CharField(max_length=50)
    drivers_license_expiry_date = models.DateField()
    drivers_license = models.FileField(upload_to='drivers_licenses/')
    psv_license_number = models.CharField(max_length=50)
    psv_license = models.FileField(upload_to='psv_licenses/')
    national_id_number = models.CharField(max_length=50)
    national_id = models.FileField(upload_to='national_ids/')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    police_clearance_certificate = models.FileField(upload_to='clearance_certificates/')
    police_clearance_number = models.CharField(max_length=50)
    
    # ForeignKey to Vehicle model
    vehicle = models.ForeignKey(
        'vehicles.Vehicle',  # vehicles app has a Vehicle model
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="drivers",
    )

    # Vehicle-related fields - removed since the reference Vehicle model is done directly
    # vehicle_registration_number = models.CharField(max_length=50)
    # vehicle_colour = models.CharField(max_length=50)
    # vehicle_insurance_policy_number = models.CharField(max_length=50)
    # vehicle_insurance_expiry_date = models.DateField()
    # vehicle_insurance = models.FileField(upload_to='vehicle_insurances/')

    driver_rating = models.FloatField(default=0)  # Average rating
    completed_rides = models.IntegerField(default=0)
    customer_review = models.TextField(null=True, blank=True)
    incident_report = models.TextField(null=True, blank=True)
    account_status = models.CharField(
        max_length=10, 
        choices=[('active', 'Active'), ('inactive', 'Inactive'), ('suspended', 'Suspended')]
    )
    date_of_account_creation = models.DateField(auto_now_add=True)
    last_active_date = models.DateField(null=True, blank=True)
    login_history = models.JSONField(default=dict)  # Store history as JSON
    payment_methods = models.JSONField(default=list)  # e.g., mobile money, cash
    earning_history = models.JSONField(default=dict)  # Store as JSON
    app_commission = models.FloatField(default=0)
    trips_made = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
