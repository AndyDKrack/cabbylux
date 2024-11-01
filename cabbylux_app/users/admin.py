# users/admin.py
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'date_joined', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'date_joined')
