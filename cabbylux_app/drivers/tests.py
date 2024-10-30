from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Driver  # Assuming `Driver` is defined in your models

# 1. Model Field Validations
class DriverModelFieldTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            first_name="Alice",
            last_name="Smith",
            email="alicesmith@example.com",
            phone_number="0712345678",
            current_residency="City A",
            driver_license_number="DL12345",
            driver_license_expiry_date="2030-01-01"
        )

    def test_first_name_label(self):
        field_label = self.driver._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_email_unique_constraint(self):
        with self.assertRaises(Exception):
            Driver.objects.create(
                first_name="Bob",
                last_name="Jones",
                email="alicesmith@example.com"  # Duplicate email
            )

    def test_phone_number_optional(self):
        driver = Driver.objects.create(
            first_name="Charlie",
            last_name="Doe",
            email="charliedoe@example.com",
            current_residency="City B",
            driver_license_number="DL67890",
            driver_license_expiry_date="2032-06-15"
        )
        self.assertEqual(driver.phone_number, None)


# 2. CRUD Operations
class DriverModelCRUDTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            first_name="Alice",
            last_name="Smith",
            email="alicesmith@example.com",
            phone_number="0712345678",
            current_residency="City A",
            driver_license_number="DL12345",
            driver_license_expiry_date="2030-01-01"
        )

    def test_create_driver(self):
        driver_count = Driver.objects.count()
        self.assertEqual(driver_count, 1)

    def test_read_driver(self):
        driver = Driver.objects.get(id=self.driver.id)
        self.assertEqual(driver.first_name, "Alice")

    def test_update_driver(self):
        self.driver.first_name = "Alicia"
        self.driver.save()
        driver = Driver.objects.get(id=self.driver.id)
        self.assertEqual(driver.first_name, "Alicia")

    def test_delete_driver(self):
        self.driver.delete()
        driver_count = Driver.objects.count()
        self.assertEqual(driver_count, 0)


# 3. Model Method Tests
class DriverModelMethodTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            first_name="Alice",
            last_name="Smith",
            email="alicesmith@example.com"
        )

    def test_str_method(self):
        self.assertEqual(str(self.driver), "Alice Smith")


# 4. Driver Authentication and Permissions (if applicable)
class DriverAuthenticationTest(TestCase):
    # Assuming some authentication or login mechanism for drivers
    def setUp(self):
        # Simulate creating a driver with login credentials if applicable
        pass

    def test_login_driver(self):
        # Placeholder for driver login tests
        pass


# 5. Validation and Edge Cases
class DriverModelValidationTest(TestCase):
    def test_first_name_max_length(self):
        driver = Driver.objects.create(
            first_name="A" * 50,  # Max length test
            last_name="Smith",
            email="alicesmith@example.com",
            current_residency="City A",
            driver_license_number="DL12345",
            driver_license_expiry_date="2030-01-01"
        )
        self.assertEqual(len(driver.first_name), 50)

    def test_invalid_email(self):
        with self.assertRaises(Exception):
            Driver.objects.create(
                first_name="Alice",
                last_name="Smith",
                email="not-an-email"  # Invalid email should raise an error
            )


# 6. API Endpoint Tests (if you have API views for Driver)
class DriverAPITest(APITestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            first_name="Alice",
            last_name="Smith",
            email="alicesmith@example.com",
            phone_number="0712345678",
            current_residency="City A",
            driver_license_number="DL12345",
            driver_license_expiry_date="2030-01-01"
        )

    def test_get_driver_list(self):
        url = reverse('driver_list')  # Assume a URL name for driver list
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_driver_via_api(self):
        url = reverse('driver_create')  # Assume a URL name for driver creation
        data = {
            "first_name": "Bob",
            "last_name": "Jones",
            "email": "bobjones@example.com",
            "phone_number": "0798765432",
            "current_residency": "City B",
            "driver_license_number": "DL98765",
            "driver_license_expiry_date": "2035-05-10"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
