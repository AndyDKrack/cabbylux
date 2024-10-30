from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Chauffeur  # Ensure `Chauffeur` is defined in your models

# 1. Model Field Validations
class ChauffeurModelFieldTest(TestCase):
    def setUp(self):
        self.chauffeur = Chauffeur.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1985-05-15",
            email="johndoe@example.com",
            phone_number="0712345678",
            residence="Nairobi",
            emergency_contact_name="Jane Doe",
            emergency_contact_phone="0798765432",
            years_of_experience=10,
            chauffeur_rating=4.5,
            account_status="active"
        )

    def test_first_name_label(self):
        field_label = self.chauffeur._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_chauffeur_rating(self):
        self.assertEqual(self.chauffeur.chauffeur_rating, 4.5)


# 2. CRUD Operations
class ChauffeurModelCRUDTest(TestCase):
    def setUp(self):
        self.chauffeur = Chauffeur.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1985-05-15",
            email="johndoe@example.com",
            phone_number="0712345678",
            residence="Nairobi",
            emergency_contact_name="Jane Doe",
            emergency_contact_phone="0798765432",
            years_of_experience=10,
            chauffeur_rating=4.5,
            account_status="active"
        )

    def test_create_chauffeur(self):
        chauffeur_count = Chauffeur.objects.count()
        self.assertEqual(chauffeur_count, 1)

    def test_read_chauffeur(self):
        chauffeur = Chauffeur.objects.get(id=self.chauffeur.id)
        self.assertEqual(chauffeur.first_name, "John")

    def test_update_chauffeur(self):
        self.chauffeur.chauffeur_rating = 4.8
        self.chauffeur.save()
        chauffeur = Chauffeur.objects.get(id=self.chauffeur.id)
        self.assertEqual(chauffeur.chauffeur_rating, 4.8)

    def test_delete_chauffeur(self):
        self.chauffeur.delete()
        chauffeur_count = Chauffeur.objects.count()
        self.assertEqual(chauffeur_count, 0)


# 3. Model Method Tests
class ChauffeurModelMethodTest(TestCase):
    def setUp(self):
        self.chauffeur = Chauffeur.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1985-05-15",
            email="johndoe@example.com",
            phone_number="0712345678"
        )

    def test_str_method(self):
        self.assertEqual(str(self.chauffeur), "John Doe")


# 4. Field Validation and Edge Cases
class ChauffeurModelValidationTest(TestCase):
    def test_invalid_phone_number(self):
        with self.assertRaises(ValueError):
            Chauffeur.objects.create(
                first_name="John",
                last_name="Doe",
                date_of_birth="1985-05-15",
                email="johndoe@example.com",
                phone_number="InvalidPhone",
                residence="Nairobi"
            )

    def test_date_of_birth(self):
        chauffeur = Chauffeur.objects.create(
            first_name="Jane",
            last_name="Smith",
            date_of_birth="1990-07-25",
            email="janesmith@example.com",
            phone_number="0711122233"
        )
        self.assertEqual(chauffeur.date_of_birth.year, 1990)


# 5. API Endpoint Tests (if you have API views for Chauffeur)
class ChauffeurAPITest(APITestCase):
    def setUp(self):
        self.chauffeur = Chauffeur.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1985-05-15",
            email="johndoe@example.com",
            phone_number="0712345678",
            residence="Nairobi",
            years_of_experience=10,
            chauffeur_rating=4.5
        )

    def test_get_chauffeur_list(self):
        url = reverse('chauffeur_list')  # Ensure to have a URL name for list endpoint
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_chauffeur_via_api(self):
        url = reverse('chauffeur_create')  # Ensure to have a URL name for creation endpoint
        data = {
            "first_name": "Alice",
            "last_name": "Johnson",
            "date_of_birth": "1988-11-15",
            "email": "alicejohnson@example.com",
            "phone_number": "0722334455",
            "residence": "Mombasa",
            "emergency_contact_name": "Bob Johnson",
            "emergency_contact_phone": "0722334466",
            "years_of_experience": 5,
            "chauffeur_rating": 4.2,
            "account_status": "active"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
