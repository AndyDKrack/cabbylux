from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PaymentViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Function-based views for Payments
    path('payment-list/', views.payment_list, name='payment_list'),
    path('payment-new/', views.payment_create, name='payment_create'),
    path('payment/<int:payment_id>/', views.payment_detail, name='payment_detail'),
    path('payment/<int:payment_id>/edit/', views.payment_update, name='payment_update'),
    path('payment/<int:payment_id>/delete/', views.payment_delete, name='payment_delete'),
]
