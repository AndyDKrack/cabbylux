from django.db import models
from vehicles.models import Vehicle 

class Chauffeur(models.Model):
    chauffeur_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    residence = models.CharField(max_length=100)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    emergency_contact_residency = models.CharField(max_length=100)
    drivers_license_number = models.CharField(max_length=50)
    drivers_license_expiry_date = models.DateField()
    drivers_license = models.FileField(upload_to='drivers_licenses/')
    psv_license_number = models.CharField(max_length=50)
    psv_license = models.FileField(upload_to='psv_licenses/')
    years_of_experience_certificate = models.FileField(upload_to='experience_certificates/')
    defensive_driving_certificate = models.FileField(upload_to='defensive_driving_certificates/')
    police_clearance_certificate = models.FileField(upload_to='clearance_certificates/')
    national_id_number = models.CharField(max_length=50)
    national_id = models.FileField(upload_to='national_ids/')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    # ForeignKey to Vehicle model
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="chauffeurs"
    )

    chauffeur_rating = models.FloatField(default=0)  # Average rating
    completed_jobs = models.IntegerField(default=0)
    customer_reviews = models.TextField(null=True, blank=True)
    reported_incidents = models.TextField(null=True, blank=True)
    account_creation_date = models.DateField(auto_now_add=True)
    account_status = models.CharField(
        max_length=10, 
        choices=[('active', 'Active'), ('inactive', 'Inactive'), ('suspended', 'Suspended')]
    )
    last_active_date = models.DateField(null=True, blank=True)
    availability = models.JSONField(default=dict)  # e.g., {"hours": 40, "days": 5}
    operating_area_preference = models.JSONField(default=list)  # e.g., ["city", "long distance"]
    languages_spoken = models.JSONField(default=list)  # e.g., ["English", "Swahili"]
    gps_tracking_enabled = models.BooleanField(default=True)
    confidentiality_permission = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
