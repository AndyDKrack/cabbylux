from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserViewSet

# Set up router for viewset
router = DefaultRouter()
router.register(r'users', UserViewSet)

# Define urlpatterns for both function-based views and viewset routes
urlpatterns = [
    path('', include(router.urls)),  # Include the viewset routes

    # Function-based views for Users
    path('user-list/', views.user_list, name='user_list'),
    path('user-new/', views.user_create, name='user_create'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user/<int:user_id>/edit/', views.user_update, name='user_update'),
    path('user/<int:user_id>/delete/', views.user_delete, name='user_delete'),
]
