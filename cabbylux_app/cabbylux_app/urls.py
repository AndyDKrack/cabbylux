"""
URL configuration for cabbylux_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin site
    path('api/users/', include('users.urls')),       # Includes URLs from the users app
    path('api/drivers/', include('drivers.urls')),   # Includes URLs from the drivers app
    path('api/chauffeurs/', include('chauffeurs.urls')),  # Includes URLs from the chauffeurs app
    path('api/vehicles/', include('vehicles.urls')),  # Includes URLs from the vehicles app
    path('api/payments/', include('payments.urls')),  # Includes URLs from the payments app
]

