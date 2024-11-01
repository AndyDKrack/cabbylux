from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DriverViewSet, driver_list, driver_detail, driver_create, driver_update, driver_delete

app_name = 'drivers'  # Namespace for drivers app

router = DefaultRouter()
router.register(r'drivers', DriverViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Function-based views for Drivers
    path('driver-list/', driver_list, name='driver_list'),
    path('driver-new/', driver_create, name='driver_create'),
    path('driver/<int:driver_id>/', driver_detail, name='driver_detail'),
    path('driver/<int:driver_id>/edit/', driver_update, name='driver_update'),
    path('driver/<int:driver_id>/delete/', driver_delete, name='driver_delete'),
]
