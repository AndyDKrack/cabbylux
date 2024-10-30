from django.test import TestCase
from django.contrib.auth.models import User as AuthUser
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User  # Assuming `User` is your custom user model

# 1. Model Field Validations
class UserModelFieldTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            residence_location="City A",
            work_location="City B"
        )

    def test_first_name_label(self):
        field_label = self.user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_email_unique_constraint(self):
        with self.assertRaises(Exception):
            User.objects.create(
                first_name="Jane",
                last_name="Smith",
                email="johndoe@example.com"  # Duplicate email should raise an error
            )

    def test_phone_number_optional(self):
        user = User.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="janedoe@example.com",
            residence_location="City A",
            work_location="City B"
        )
        self.assertEqual(user.phone_number, None)


# 2. CRUD Operations
class UserModelCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            residence_location="City A",
            work_location="City B"
        )

    def test_create_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_read_user(self):
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.first_name, "John")

    def test_update_user(self):
        self.user.first_name = "Jane"
        self.user.save()
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.first_name, "Jane")

    def test_delete_user(self):
        self.user.delete()
        user_count = User.objects.count()
        self.assertEqual(user_count, 0)


# 3. Model Method Tests
class UserModelMethodTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com"
        )

    def test_str_method(self):
        self.assertEqual(str(self.user), "John Doe")


# 4. User Authentication and Permissions
class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.auth_user = AuthUser.objects.create_user(username="johndoe", password="password123")

    def test_login_user(self):
        login = self.client.login(username="johndoe", password="password123")
        self.assertTrue(login)

    def test_failed_login(self):
        login = self.client.login(username="johndoe", password="wrongpassword")
        self.assertFalse(login)


# 5. Validation and Edge Cases
class UserModelValidationTest(TestCase):
    def test_first_name_max_length(self):
        user = User.objects.create(
            first_name="A" * 50,  # Max length
            last_name="Doe",
            email="johndoe@example.com",
            residence_location="City A",
            work_location="City B"
        )
        self.assertEqual(len(user.first_name), 50)

    def test_invalid_email(self):
        with self.assertRaises(Exception):
            User.objects.create(
                first_name="John",
                last_name="Doe",
                email="not-an-email"  # Invalid email should raise an error
            )


# 6. API Endpoint Tests (if you have API views for User)
class UserAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            residence_location="City A",
            work_location="City B"
        )

    def test_get_user_list(self):
        url = reverse('user_list')  # Assume a URL name for user list
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user_via_api(self):
        url = reverse('user_create')  # Assume a URL name for user create
        data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "janesmith@example.com",
            "residence_location": "City X",
            "work_location": "City Y"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
