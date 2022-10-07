from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *
from .forms import UserCreationForm, SecurityCreationForm, SupervisorCreationForm


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    list_filter = ()
    ordering = ('email',)
    filter_horizontal = ('user_permissions',)
    
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'phone'
    )
    
    readonly_fields = (
        'uuid',
        'last_login',
        'created_date'
    )
    
    list_display = (
        'email',
        'first_name',
        'last_name',
        'phone',
        'is_active',
        'is_resident',
        'is_security',
        'is_supervisor',
        'is_residenceadmin',
        'is_condoadmin',
        'is_agencyadmin',
        'is_platformadmin',
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
                'user_permissions',
            )
        }),
        ('Roles', {
            'fields': (
                'is_active',
                'is_resident',
                'is_security',
                'is_supervisor',
                'is_residenceadmin',
                'is_condoadmin',
                'is_agencyadmin',
                'is_platformadmin',
                'is_staff',
                'is_superuser',
            )
        }),
        ('Misc', {
            'fields': (
                'uuid',
                'last_login',
                'created_date'
            )
        }),
    )
    
    add_fieldsets = (
        ('Credentials', {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
            ),
        }),
        ('Roles', {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                'is_resident',
                'is_security',
                'is_supervisor',
                'is_residenceadmin',
                'is_condoadmin',
                'is_agencyadmin',
                'is_platformadmin',
                'is_staff',
                'is_superuser',
            )
        }),
    )


@admin.register(
    AgencyAdmin,
    CondoAdmin,
    PlatformAdmin,
    ResidenceAdmin,
)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = (
        'get_email',
        'get_first_name',
        'get_last_name',
        'get_phone',
        'get_address',
        'get_is_active',
        'get_last_login',
        'get_created_date',
    )
    
    @admin.display(ordering='user__email', description='email')
    def get_email(self, obj):
        return obj.user.email
    
    @admin.display(ordering='user__first_name', description='first name')
    def get_first_name(self, obj):
        return obj.user.first_name
    
    @admin.display(ordering='user__last_name', description='last name')
    def get_last_name(self, obj):
        return obj.user.last_name
    
    @admin.display(ordering='user__phone', description='phone')
    def get_phone(self, obj):
        return obj.user.phone
    
    @admin.display(ordering='user__address', description='address')
    def get_address(self, obj):
        return obj.user.address
    
    @admin.display(ordering='user__is_active', description='active', boolean=True)
    def get_is_active(self, obj):
        return obj.user.is_active
    
    @admin.display(ordering='user__last_login', description='last login')
    def get_last_login(self, obj):
        return obj.user.last_login
    
    @admin.display(ordering='user__created_date', description='created date')
    def get_created_date(self, obj):
        return obj.user.created_date


@admin.register(
    Security,
    Supervisor
)
class SecurityType(admin.ModelAdmin):
    list_display = (
        'get_email',
        'get_first_name',
        'get_last_name',
        'get_phone',
        'get_address',
        'get_is_active',
        'get_last_login',
        'get_created_date',
        'agency'
    )
    
    @admin.display(ordering='user__email', description='email')
    def get_email(self, obj):
        return obj.user.email
    
    @admin.display(ordering='user__first_name', description='first name')
    def get_first_name(self, obj):
        return obj.user.first_name
    
    @admin.display(ordering='user__last_name', description='last name')
    def get_last_name(self, obj):
        return obj.user.last_name
    
    @admin.display(ordering='user__phone', description='phone')
    def get_phone(self, obj):
        return obj.user.phone
    
    @admin.display(ordering='user__address', description='address')
    def get_address(self, obj):
        return obj.user.address
    
    @admin.display(ordering='user__is_active', description='active', boolean=True)
    def get_is_active(self, obj):
        return obj.user.is_active
    
    @admin.display(ordering='user__last_login', description='last login')
    def get_last_login(self, obj):
        return obj.user.last_login
    
    @admin.display(ordering='user__created_date', description='created date')
    def get_created_date(self, obj):
        return obj.user.created_date

    def get_form(self, request, obj=None, change=False, **kwargs):
        if self.model is Security:
            form = SecurityCreationForm
        elif self.model is Supervisor:
            form = SupervisorCreationForm
            form.connected_user = request.user

            return form


@admin.register(
    Resident,
)
class SecurityType(admin.ModelAdmin):
    list_display = (
        'get_email',
        'get_first_name',
        'get_last_name',
        'get_phone',
        'get_address',
        'get_is_active',
        'get_last_login',
        'get_created_date',
        'residence'
    )
    
    @admin.display(ordering='user__email', description='email')
    def get_email(self, obj):
        return obj.user.email
    
    @admin.display(ordering='user__first_name', description='first name')
    def get_first_name(self, obj):
        return obj.user.first_name
    
    @admin.display(ordering='user__last_name', description='last name')
    def get_last_name(self, obj):
        return obj.user.last_name
    
    @admin.display(ordering='user__phone', description='phone')
    def get_phone(self, obj):
        return obj.user.phone
    
    @admin.display(ordering='user__address', description='address')
    def get_address(self, obj):
        return obj.user.address
    
    @admin.display(ordering='user__is_active', description='active', boolean=True)
    def get_is_active(self, obj):
        return obj.user.is_active
    
    @admin.display(ordering='user__last_login', description='last login')
    def get_last_login(self, obj):
        return obj.user.last_login
    
    @admin.display(ordering='user__created_date', description='created date')
    def get_created_date(self, obj):
        return obj.user.created_date