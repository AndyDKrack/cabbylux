from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),  # List view
    path('new/', views.vehicle_create, name='vehicle_create'),  # Create view
    path('<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),  # Detail view
    path('<int:vehicle_id>/edit/', views.vehicle_update, name='vehicle_update'),  # Update view
    path('<int:vehicle_id>/delete/', views.vehicle_delete, name='vehicle_delete'),  # Delete view
]
