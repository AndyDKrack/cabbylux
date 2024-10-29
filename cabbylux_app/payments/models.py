from django.db import models

class Payment(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    booking_id = models.CharField(max_length=50)
    date_and_time = models.DateTimeField(auto_now_add=True)
    amount_paid = models.FloatField()
    payment_status = models.CharField(max_length=20, choices=[('completed', 'Completed'), ('pending', 'Pending'), ('failed', 'Failed'), ('refunded', 'Refunded')])
    customer_id = models.ForeignKey('users.User', on_delete=models.CASCADE)  # Link to User
    customer_name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)  # e.g., phone number
    billing_address = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=20, choices=[('mobile money', 'Mobile Money'), ('cash', 'Cash')])
    invoice_number = models.CharField(max_length=50)
    date_of_invoice = models.DateField()
    charges_list = models.JSONField(default=dict)  # e.g., {"service_charge": 5, "tax": 2}
    total_amount_due = models.FloatField()
    total_amount_paid = models.FloatField()
    linked_driver_or_chauffeur_id = models.CharField(max_length=50)  # To link to Driver or Chauffeur
    amount_earned = models.FloatField()
    commission_rate_deducted = models.FloatField()
    transaction_logs = models.TextField(null=True, blank=True)  # For logs
    admin_notes = models.TextField(null=True, blank=True)
    dispute_status = models.CharField(max_length=20, choices=[('open', 'Open'), ('resolved', 'Resolved'), ('declined', 'Declined')])
    dispute_details = models.TextField(null=True, blank=True)
    usage_insights = models.JSONField(default=dict)  # e.g., {"ride_duration": 30, "frequency": 2}
    refund_status = models.CharField(max_length=20, choices=[('processed', 'Processed'), ('pending', 'Pending'), ('declined', 'Declined')])
    refund_amount = models.FloatField(null=True, blank=True)
    refund_reason = models.TextField(null=True, blank=True)
    refund_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.amount_paid} {self.payment_status}"
