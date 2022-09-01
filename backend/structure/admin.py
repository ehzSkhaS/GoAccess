from django.contrib import admin

from .models import(
    Agency,
    Area,
    # CommercialCondo,
    Condo,
    Platform,
    Residence,
    ResidentialCondo
)


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
        'get_number',
        'get_created',
        'get_updated',
        'get_end',
        'get_quantity',
        'get_state',
        'get_platform'
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


@admin.register(Condo)
class CondoType(admin.ModelAdmin):
    list_display = (
        'description',
        'address',
        'email',
        'phone',
        'is_residential',
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
    
    
# @admin.register(ResidentialCondo)
# class ResidentialCondoType(admin.ModelAdmin):
#     list_display = (
#         'get_description',
#         'get_address',
#         'get_email',
#         'get_phone',
#         'get_admin_email',
#         'get_is_active',
#         'get_last_login',
#         'get_agency'
#     )
    
#     @admin.display(ordering='condo__description', description='description')
#     def get_description(self, obj):
#         return obj.condo.description
    
#     @admin.display(ordering='condo__address', description='address')
#     def get_address(self, obj):
#         return obj.condo.address
    
#     @admin.display(ordering='condo__email', description='email')
#     def get_email(self, obj):
#         return obj.condo.email
    
#     @admin.display(ordering='condo__phone', description='phone')
#     def get_phone(self, obj):
#         return obj.condo.phone
    
#     @admin.display(ordering='condo__owner__user__email', description='admin email')
#     def get_admin_email(self, obj):
#         return obj.condo.owner.user.email
    
#     @admin.display(ordering='condo__owner__user__is_active', description='active', boolean=True)
#     def get_is_active(self, obj):
#         return obj.condo.owner.user.is_active
    
#     @admin.display(ordering='condo__owner__user__last_login', description='last login')
#     def get_last_login(self, obj):
#         return obj.condo.owner.user.last_login
    
#     @admin.display(ordering='condo__agency__name', description='agency')
#     def get_agency(self, obj):
#         return obj.condo.agency.name
    
@admin.register(Area)
class AreaType(admin.ModelAdmin):
    list_display = (
        'name',
        'max_people',
        'is_open',
        'get_condo'
    )
    
    @admin.display(ordering='residencialcondo__description', description='condo')
    def get_condo(self, obj):
        return obj.condo.description

    

@admin.register(Residence)
class ResidenceType(admin.ModelAdmin):
    list_display = (
        'description',
        'number',
        'street',
        'get_email',
        'get_is_active',
        'get_last_login',
        'get_condo'
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
    
    @admin.display(ordering='residencialcondo__description', description='condo')
    def get_condo(self, obj):
        return obj.condo.description
    