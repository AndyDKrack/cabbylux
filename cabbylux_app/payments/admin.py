# users/admin.py
from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'payment_date', 'status')
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'payment_date')

