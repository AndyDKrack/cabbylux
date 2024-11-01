# In payments/serializers.py
from rest_framework import serializers
from .models import Payment  # Adjust this import based on your Payment model's location

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'transaction_id', 'booking_id', 'date_and_time', 'amount_paid', 
            'payment_status', 'customer_id', 'customer_name', 'contact_information', 
            'billing_address', 'payment_method', 'invoice_number', 'date_of_invoice', 
            'charges_list', 'total_amount_due', 'total_amount_paid', 
            'linked_driver_or_chauffeur_id', 'amount_earned', 'commission_rate_deducted', 'transaction_logs', 
            'admin_notes', 'dispute_status', 'dispute_details', 
            'usage_insights', 'refund_status', 'refund_amount', 'refund_reason', 'refund_date'
        ]
