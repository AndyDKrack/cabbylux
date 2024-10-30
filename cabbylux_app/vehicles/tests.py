from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Vehicle  # Ensure `Vehicle` is defined in your models

# 1. Model Field Validations
class VehicleModelFieldTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            make="Toyota",
            model="Camry",
            year_of_manufacture=2019,
            vehicle_class_type="Sedan",
            number_plate="KDA 123A",
            color="Blue",
            seating_capacity=5,
            fuel_type="Petrol",
            engine_capacity=2.5
        )

    def test_make_label(self):
        field_label = self.vehicle._meta.get_field('make').verbose_name
        self.assertEqual(field_label, 'make')

    def test_year_of_manufacture(self):
        self.assertEqual(self.vehicle.year_of_manufacture, 2019)


# 2. CRUD Operations
class VehicleModelCRUDTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            make="Toyota",
            model="Camry",
            year_of_manufacture=2019,
            vehicle_class_type="Sedan",
            number_plate="KDA 123A",
            color="Blue"
        )

    def test_create_vehicle(self):
        vehicle_count = Vehicle.objects.count()
        self.assertEqual(vehicle_count, 1)

    def test_read_vehicle(self):
        vehicle = Vehicle.objects.get(id=self.vehicle.id)
        self.assertEqual(vehicle.make, "Toyota")

    def test_update_vehicle(self):
        self.vehicle.color = "Red"
        self.vehicle.save()
        vehicle = Vehicle.objects.get(id=self.vehicle.id)
        self.assertEqual(vehicle.color, "Red")

    def test_delete_vehicle(self):
        self.vehicle.delete()
        vehicle_count = Vehicle.objects.count()
        self.assertEqual(vehicle_count, 0)


# 3. Model Method Tests
class VehicleModelMethodTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            make="Toyota",
            model="Camry",
            year_of_manufacture=2019
        )

    def test_str_method(self):
        self.assertEqual(str(self.vehicle), "Toyota Camry 2019")


# 4. Field Validation and Edge Cases
class VehicleModelValidationTest(TestCase):
    def test_number_plate_max_length(self):
        vehicle = Vehicle.objects.create(
            make="Toyota",
            model="Camry",
            year_of_manufacture=2019,
            vehicle_class_type="Sedan",
            number_plate="KDA1234567890",
            color="Blue"
        )
        self.assertEqual(len(vehicle.number_plate), 13)

    def test_invalid_year_of_manufacture(self):
        with self.assertRaises(ValueError):
            Vehicle.objects.create(
                make="Toyota",
                model="Camry",
                year_of_manufacture=2100,  # Future year should raise an error
                vehicle_class_type="Sedan",
                number_plate="KDA123A",
                color="Blue"
            )


# 5. API Endpoint Tests (if you have API views for Vehicle)
class VehicleAPITest(APITestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            make="Toyota",
            model="Camry",
            year_of_manufacture=2019,
            vehicle_class_type="Sedan",
            number_plate="KDA 123A",
            color="Blue"
        )

    def test_get_vehicle_list(self):
        url = reverse('vehicle_list')  # Assume a URL name for vehicle list
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vehicle_via_api(self):
        url = reverse('vehicle_create')  # Assume a URL name for vehicle creation
        data = {
            "make": "Honda",
            "model": "Civic",
            "year_of_manufacture": 2020,
            "vehicle_class_type": "Sedan",
            "number_plate": "KDB 567B",
            "color": "Black",
            "seating_capacity": 5,
            "fuel_type": "Petrol",
            "engine_capacity": 2.0
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
