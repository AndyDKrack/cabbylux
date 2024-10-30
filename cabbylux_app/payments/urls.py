from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),  # List view
    path('new/', views.payment_create, name='payment_create'),  # Create view
    path('<int:payment_id>/', views.payment_detail, name='payment_detail'),  # Detail view
    path('<int:payment_id>/edit/', views.payment_update, name='payment_update'),  # Update view
    path('<int:payment_id>/delete/', views.payment_delete, name='payment_delete'),  # Delete view
]
