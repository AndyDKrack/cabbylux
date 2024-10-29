from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    residence_location = models.CharField(max_length=100)
    work_location = models.CharField(max_length=100)
    add_location = models.CharField(max_length=100, null=True, blank=True)
    number_of_trips_taken = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
