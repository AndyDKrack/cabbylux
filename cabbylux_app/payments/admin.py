# users/admin.py
from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'customer_name', 'amount_paid', 'date_and_time',)
    search_fields = ('linked_driver_or_chauffeur', 'amount_earned', 'commission_rate_deducted')
    list_filter = ('transaction_id', 'amount_paid')

