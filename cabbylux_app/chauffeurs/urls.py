from django.urls import path
from . import views

urlpatterns = [
    path('', views.chauffeur_list, name='chauffeur_list'),  # List view
    path('new/', views.chauffeur_create, name='chauffeur_create'),  # Create view
    path('<int:chauffeur_id>/', views.chauffeur_detail, name='chauffeur_detail'),  # Detail view
    path('<int:chauffeur_id>/edit/', views.chauffeur_update, name='chauffeur_update'),  # Update view
    path('<int:chauffeur_id>/delete/', views.chauffeur_delete, name='chauffeur_delete'),  # Delete view
]
