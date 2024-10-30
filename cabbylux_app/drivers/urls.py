from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import DriverViewSet

router = DefaultRouter()
router.register(r'drivers', DriverViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Function-based views for Drivers
    path('driver-list/', views.driver_list, name='driver_list'),
    path('driver-new/', views.driver_create, name='driver_create'),
    path('driver/<int:driver_id>/', views.driver_detail, name='driver_detail'),
    path('driver/<int:driver_id>/edit/', views.driver_update, name='driver_update'),
    path('driver/<int:driver_id>/delete/', views.driver_delete, name='driver_delete'),
]
