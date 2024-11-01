from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, payment_list, payment_detail, payment_create, payment_update, payment_delete

app_name = 'payments'  # Namespace for payments app

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Function-based views for Payments
    path('payment-list/', payment_list, name='payment_list'),
    path('payment-new/', payment_create, name='payment_create'),
    path('payment/<int:payment_id>/', payment_detail, name='payment_detail'),
    path('payment/<int:payment_id>/edit/', payment_update, name='payment_update'),
    path('payment/<int:payment_id>/delete/', payment_delete, name='payment_delete'),
]
