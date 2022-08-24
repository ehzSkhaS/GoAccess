from django.contrib import admin

from .models import(
    Agency,
    CommercialCondo,
    Platform,
    Residence,
    ResidencialCondo
)


# admin.site.register(Condo)
# admin.site.register(ResidencialCondo)
admin.site.register(Residence)


@admin.register(Platform)
class PlatformType(admin.ModelAdmin):
    list_display = (
        'name',
        'get_email',
        'get_is_active',
        'get_last_login',
        'get_number',
        'get_created',
        'get_updated',
        'get_end',
        'get_quantity',
        'get_state'
    )
    
    @admin.display(ordering='owner__user__email', description='admin email')
    def get_email(self, obj):
        return obj.owner.user.email
    
    @admin.display(ordering='owner__user__is_active', description='active', boolean=True)
    def get_is_active(self, obj):
        return obj.owner.user.is_active
    
    @admin.display(ordering='owner__user__last_login', description='last login')
    def get_last_login(self, obj):
        return obj.owner.user.last_login
    
    @admin.display(ordering='lic__pk', description='lic number')
    def get_number(self, obj):
        return obj.lic.pk
    
    @admin.display(ordering='lic__created', description='lic creation date')
    def get_created(self, obj):
        return obj.lic.created
    
    @admin.display(ordering='lic__updated', description='lic updated date')
    def get_updated(self, obj):
        return obj.lic.updated
    
    @admin.display(ordering='lic__end', description='lic end date')
    def get_end(self, obj):
        return obj.lic.end
    
    @admin.display(ordering='lic__quantity', description='lic allowed quantity')
    def get_quantity(self, obj):
        return obj.lic.quantity
    
    @admin.display(ordering='lic__state', description='lic state', boolean=True)
    def get_state(self, obj):
        return obj.lic.state
    
    
@admin.register(Agency)
class AgencyType(admin.ModelAdmin):
    list_display = (
        'name',
        'get_email',
        'get_is_active',
        'get_last_login',
        'get_platform',
        'get_number',
        'get_created',
        'get_updated',
        'get_end',
        'get_quantity',
        'get_state'
    )
    
    @admin.display(ordering='owner__user__email', description='admin email')
    def get_email(self, obj):
        return obj.owner.user.email
    
    @admin.display(ordering='owner__user__is_active', description='active', boolean=True)
    def get_is_active(self, obj):
        return obj.owner.user.is_active
    
    @admin.display(ordering='owner__user__last_login', description='last login')
    def get_last_login(self, obj):
        return obj.owner.user.last_login
    
    @admin.display(ordering='lic__pk', description='lic number')
    def get_number(self, obj):
        return obj.lic.pk
    
    @admin.display(ordering='lic__created', description='lic creation date')
    def get_created(self, obj):
        return obj.lic.created
    
    @admin.display(ordering='lic__updated', description='lic updated date')
    def get_updated(self, obj):
        return obj.lic.updated
    
    @admin.display(ordering='lic__end', description='lic end date')
    def get_end(self, obj):
        return obj.lic.end
    
    @admin.display(ordering='lic__quantity', description='lic allowed quantity')
    def get_quantity(self, obj):
        return obj.lic.quantity
    
    @admin.display(ordering='lic__state', description='lic state', boolean=True)
    def get_state(self, obj):
        return obj.lic.state
    
    @admin.display(ordering='platform__name', description='platform')
    def get_platform(self, obj):
        return obj.platform.name


@admin.register(
    CommercialCondo,
    ResidencialCondo
)
class CondoType(admin.ModelAdmin):
    list_display = (
        'description',
        'address',
        'email',
        'phone',
        'get_email',
        'get_is_active',
        'get_last_login',
        'get_agency'
    )
    
    @admin.display(ordering='owner__user__email', description='admin email')
    def get_email(self, obj):
        return obj.owner.user.email
    
    @admin.display(ordering='owner__user__is_active', description='active', boolean=True)
    def get_is_active(self, obj):
        return obj.owner.user.is_active
    
    @admin.display(ordering='owner__user__last_login', description='last login')
    def get_last_login(self, obj):
        return obj.owner.user.last_login
    
    @admin.display(ordering='agency__name', description='agency')
    def get_agency(self, obj):
        return obj.agency.name
    
    