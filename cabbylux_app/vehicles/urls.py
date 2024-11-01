from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, vehicle_list, vehicle_detail, vehicle_create, vehicle_update, vehicle_delete

app_name = 'vehicles'  # Namespace for vehicles app

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Function-based views for Vehicles
    path('vehicle-list/', vehicle_list, name='vehicle_list'),
    path('vehicle-new/', vehicle_create, name='vehicle_create'),
    path('vehicle/<int:vehicle_id>/', vehicle_detail, name='vehicle_detail'),
    path('vehicle/<int:vehicle_id>/edit/', vehicle_update, name='vehicle_update'),
    path('vehicle/<int:vehicle_id>/delete/', vehicle_delete, name='vehicle_delete'),
]
