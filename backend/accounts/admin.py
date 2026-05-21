from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'phone', 'created_at')
    search_fields = ('email', 'full_name', 'phone')
