from django.urls import path
from . import views

urlpatterns = [
    path('', views.driver_list, name='driver_list'),  # List view
    path('new/', views.driver_create, name='driver_create'),  # Create view
    path('<int:driver_id>/', views.driver_detail, name='driver_detail'),  # Detail view
    path('<int:driver_id>/edit/', views.driver_update, name='driver_update'),  # Update view
    path('<int:driver_id>/delete/', views.driver_delete, name='driver_delete'),  # Delete view
]
