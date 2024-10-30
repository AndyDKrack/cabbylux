# In payments/serializers.py
from rest_framework import serializers
from .models import Payment  # Adjust this import based on your Payment model's location

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'transaction_id', 'booking_id', 'date_time_of_transaction', 'amount_paid', 
            'payment_status', 'customer_id', 'customer_name', 'contact_information', 
            'billing_address', 'payment_method', 'invoice_number', 'date_of_invoice', 
            'list_of_charges', 'tax_or_additional_fees', 'total_amount_due_and_paid', 
            'linked_entity_id', 'amount_earned', 'commission_rate_deducted', 'payment_status', 
            'transaction_logs', 'admin_user_notes', 'dispute_status', 'dispute_details', 
            'usage_insights', 'refund_status', 'refund_amount', 'reason_for_refund', 'refund_date'
        ]
