from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Payment, User, Driver, Chauffeur, Vehicle  # Ensure these are defined in your models
from datetime import datetime

# 1. Model Field Validations
class PaymentModelFieldTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phone_number="0712345678"
        )
        self.payment = Payment.objects.create(
            transaction_id="TX12345",
            booking_id="BK54321",
            amount_paid=5000.0,
            payment_status="completed",
            user=self.user,
            payment_method="mobile money",
            transaction_date=datetime.now()
        )

    def test_transaction_id_label(self):
        field_label = self.payment._meta.get_field('transaction_id').verbose_name
        self.assertEqual(field_label, 'transaction id')

    def test_payment_status(self):
        self.assertEqual(self.payment.payment_status, "completed")


# 2. CRUD Operations
class PaymentModelCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Jane Doe",
            email="janedoe@example.com",
            phone_number="0712345679"
        )
        self.payment = Payment.objects.create(
            transaction_id="TX54321",
            booking_id="BK12345",
            amount_paid=3000.0,
            payment_status="pending",
            user=self.user,
            payment_method="cash",
            transaction_date=datetime.now()
        )

    def test_create_payment(self):
        payment_count = Payment.objects.count()
        self.assertEqual(payment_count, 1)

    def test_read_payment(self):
        payment = Payment.objects.get(id=self.payment.id)
        self.assertEqual(payment.transaction_id, "TX54321")

    def test_update_payment(self):
        self.payment.payment_status = "completed"
        self.payment.save()
        payment = Payment.objects.get(id=self.payment.id)
        self.assertEqual(payment.payment_status, "completed")

    def test_delete_payment(self):
        self.payment.delete()
        payment_count = Payment.objects.count()
        self.assertEqual(payment_count, 0)


# 3. Model Method Tests (if any methods are defined for Payment)
class PaymentModelMethodTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phone_number="0712345678"
        )
        self.payment = Payment.objects.create(
            transaction_id="TX12345",
            booking_id="BK54321",
            amount_paid=5000.0,
            payment_status="completed",
            user=self.user,
            payment_method="mobile money",
            transaction_date=datetime.now()
        )

    def test_str_method(self):
        self.assertEqual(str(self.payment), "TX12345 - completed")


# 4. Field Validation and Edge Cases
class PaymentModelValidationTest(TestCase):
    def test_invalid_payment_status(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(
                transaction_id="TX99999",
                booking_id="BK99999",
                amount_paid=2000.0,
                payment_status="invalid_status",  # invalid value
                payment_method="cash",
                transaction_date=datetime.now()
            )

    def test_negative_amount_paid(self):
        with self.assertRaises(ValueError):
            Payment.objects.create(
                transaction_id="TX88888",
                booking_id="BK88888",
                amount_paid=-500.0,  # invalid negative amount
                payment_status="completed",
                payment_method="mobile money",
                transaction_date=datetime.now()
            )


# 5. API Endpoint Tests (if you have API views for Payment)
class PaymentAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Alice Johnson",
            email="alicejohnson@example.com",
            phone_number="0722334455"
        )
        self.payment = Payment.objects.create(
            transaction_id="TX11223",
            booking_id="BK33445",
            amount_paid=4500.0,
            payment_status="completed",
            user=self.user,
            payment_method="cash",
            transaction_date=datetime.now()
        )

    def test_get_payment_list(self):
        url = reverse('payment_list')  # Ensure to have a URL name for list endpoint
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_payment_via_api(self):
        url = reverse('payment_create')  # Ensure to have a URL name for creation endpoint
        data = {
            "transaction_id": "TX99887",
            "booking_id": "BK77889",
            "amount_paid": 5000.0,
            "payment_status": "completed",
            "user": self.user.id,
            "payment_method": "mobile money",
            "transaction_date": datetime.now().isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
