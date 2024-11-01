from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChauffeurViewSet, chauffeur_list, chauffeur_detail, chauffeur_create, chauffeur_update, chauffeur_delete

app_name = 'chauffeurs'  # Namespace for chauffeurs app

router = DefaultRouter()
router.register(r'chauffeurs', ChauffeurViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Function-based views for Chauffeurs
    path('chauffeur-list/', chauffeur_list, name='chauffeur_list'),
    path('chauffeur-new/', chauffeur_create, name='chauffeur_create'),
    path('chauffeur/<int:chauffeur_id>/', chauffeur_detail, name='chauffeur_detail'),
    path('chauffeur/<int:chauffeur_id>/edit/', chauffeur_update, name='chauffeur_update'),
    path('chauffeur/<int:chauffeur_id>/delete/', chauffeur_delete, name='chauffeur_delete'),
]
