# Generated by Django 5.1.2 on 2024-10-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('current_residency', models.CharField(max_length=100)),
                ('emergency_contact_name', models.CharField(max_length=100)),
                ('emergency_contact_phone', models.CharField(max_length=15)),
                ('drivers_license_number', models.CharField(max_length=50)),
                ('drivers_license_expiry_date', models.DateField()),
                ('drivers_license', models.FileField(upload_to='drivers_licenses/')),
                ('psv_license_number', models.CharField(max_length=50)),
                ('psv_license', models.FileField(upload_to='psv_licenses/')),
                ('national_id_number', models.CharField(max_length=50)),
                ('national_id', models.FileField(upload_to='national_ids/')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('police_clearance_certificate', models.FileField(upload_to='clearance_certificates/')),
                ('police_clearance_number', models.CharField(max_length=50)),
                ('vehicle_details', models.CharField(max_length=255)),
                ('vehicle_registration_number', models.CharField(max_length=50)),
                ('vehicle_colour', models.CharField(max_length=50)),
                ('vehicle_insurance_policy_number', models.CharField(max_length=50)),
                ('vehicle_insurance_expiry_date', models.DateField()),
                ('vehicle_insurance', models.FileField(upload_to='vehicle_insurances/')),
                ('driver_rating', models.FloatField(default=0)),
                ('completed_rides', models.IntegerField(default=0)),
                ('customer_review', models.TextField(blank=True, null=True)),
                ('incident_report', models.TextField(blank=True, null=True)),
                ('account_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('suspended', 'Suspended')], max_length=10)),
                ('date_of_account_creation', models.DateField(auto_now_add=True)),
                ('last_active_date', models.DateField(blank=True, null=True)),
                ('login_history', models.JSONField(default=dict)),
                ('payment_methods', models.JSONField(default=list)),
                ('earning_history', models.JSONField(default=dict)),
                ('app_commission', models.FloatField(default=0)),
                ('trips_made', models.IntegerField(default=0)),
            ],
        ),
    ]
