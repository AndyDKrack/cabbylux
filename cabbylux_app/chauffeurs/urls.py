from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ChauffeurViewSet

router = DefaultRouter()
router.register(r'chauffeurs', ChauffeurViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Function-based views for Chauffeurs
    path('chauffeur-list/', views.chauffeur_list, name='chauffeur_list'),
    path('chauffeur-new/', views.chauffeur_create, name='chauffeur_create'),
    path('chauffeur/<int:chauffeur_id>/', views.chauffeur_detail, name='chauffeur_detail'),
    path('chauffeur/<int:chauffeur_id>/edit/', views.chauffeur_update, name='chauffeur_update'),
    path('chauffeur/<int:chauffeur_id>/delete/', views.chauffeur_delete, name='chauffeur_delete'),
]
