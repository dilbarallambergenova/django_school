# school/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Subject,Teacher

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Rol tanlash', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol tanlash', {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subject)
admin.site.register(Teacher)