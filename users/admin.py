from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }
    list_display = ('username', 'email', 'full_name', 'phone', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'full_name', 'phone')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    ordering = ('username',)

    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {
            'fields': ('full_name', 'phone', 'avatar')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительно', {
            'fields': ('full_name', 'phone', 'email', 'avatar')
        }),
    )
