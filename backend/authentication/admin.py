from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('user_permissions',)
    list_filter = ('is_superuser',)
    
    list_display = (
        'email',
        'first_name',
        'last_name',
        'phone',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'created_date'
    )
    
    fieldsets = (
        ('Login', {
            'fields': (
                    'email',
                    'password'
            )
        }),
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',
                'phone',
                'address',
                'image'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'user_permissions',
            )
        }),
    )
    
    add_fieldsets = (
        ('Credentials', {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2'
            ),
        }),
    )



""" 
    def has_add_permission(self, request):
        if (request.user.is_superuser):
            return True
    
    def has_change_permission(self, request, obj=None):
        if (request.user.is_superuser or request.user == obj):
            return True
    
    def has_delete_permission(self, request, obj=None):
        if (request.user.is_superuser or request.user == obj):
            return True
    
    def has_view_permission(self, request, obj=None):
        if (request.user.is_staff):
            return True
 """