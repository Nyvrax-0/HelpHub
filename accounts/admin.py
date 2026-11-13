from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (("HelpHub", {"fields": ("role", "city", "phone")}),)
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (("HelpHub", {"fields": ("email", "role", "city", "phone")}),)
    list_display = ("username", "email", "role", "city", "is_staff")
    list_filter = DjangoUserAdmin.list_filter + ("role",)
