# users/admin.py
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'email')
    list_filter = ('first_name', 'last_name')
