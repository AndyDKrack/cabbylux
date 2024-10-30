from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),  # List view
    path('new/', views.user_create, name='user_create'),  # Create view
    path('<int:user_id>/', views.user_detail, name='user_detail'),  # Detail view
    path('<int:user_id>/edit/', views.user_update, name='user_update'),  # Update view
    path('<int:user_id>/delete/', views.user_delete, name='user_delete'),  # Delete view
]
