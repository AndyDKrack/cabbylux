# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, user_list, user_detail, user_create, user_update, user_delete

app_name = 'users'  # Set the namespace for this app

# Set up the router for the ViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # Include the ViewSet URLs
    path('', include(router.urls)),

    # Define URL patterns for the function-based views (FBVs) with unique names for namespacing
    path('user-list/', user_list, name='user_list'),  # List view
    path('user-new/', user_create, name='user_create'),  # Create view
    path('user/<int:user_id>/', user_detail, name='user_detail'),  # Detail view
    path('user/<int:user_id>/edit/', user_update, name='user_update'),  # Update view
    path('user/<int:user_id>/delete/', user_delete, name='user_delete'),  # Delete view
]


