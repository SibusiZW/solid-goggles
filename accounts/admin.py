from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Add your custom fields to the admin forms
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('student_id', 'student_class')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('student_id', 'student_class')}),
    )
    # Ensure the admin displays your custom USERNAME_FIELD
    ordering = ('student_id',)
    list_display = ('student_id', 'email', 'is_staff')

admin.site.register(User, UserAdmin)
