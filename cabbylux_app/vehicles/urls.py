from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import VehicleViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Function-based views for Vehicles
    path('vehicle-list/', views.vehicle_list, name='vehicle_list'),
    path('vehicle-new/', views.vehicle_create, name='vehicle_create'),
    path('vehicle/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicle/<int:vehicle_id>/edit/', views.vehicle_update, name='vehicle_update'),
    path('vehicle/<int:vehicle_id>/delete/', views.vehicle_delete, name='vehicle_delete'),
]
