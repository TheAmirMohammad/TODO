from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('id', 'email', 'username', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'age', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name','last_name', 'birthday')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name','last_name', 'birthday', 'password1', 'password2','is_active', 'is_staff')}
         ),
    )

admin.site.register(User, UserAdminConfig)