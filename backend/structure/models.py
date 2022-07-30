from django.db import models

from authentication.models import *

class LicenseState(models.Model):
    LIC_STATES = (
        ('1', 'Enabled'),
        ('2', 'Disabled'),
    )    
    state = models.CharField(max_length=10, choices=LIC_STATES)
    
    class Meta:
        db_table = 'license_state'
        verbose_name = "License State"
        verbose_name_plural = "License States"
        
    def __str__(self):
        return str(self.state)
    
    
class License(models.Model):
    created = models.DateField(auto_now_add=True, null=False)
    udated = models.DateField(auto_now=True)
    ended = models.DateField(null=False)
    quantity = models.IntegerField(default=5)
    licstate_id = models.ForeignKey(LicenseState, on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'license'
        verbose_name = "License"
        verbose_name_plural = "Licenses"
        
    def __str__(self):
        return str(self.ended)


class Platform(models.Model):
    platformadmin = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    lic = models.OneToOneField(License, null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'platform'
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"
        
    def __str__(self):
        return str(self.platformadmin)


class Agency(models.Model):
    agencyadmin = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    lic = models.OneToOneField(License, null=False, on_delete=models.CASCADE)
    platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'agency'
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"
        
    def __str__(self):
        return str(self.agencyadmin)
    
    
class Condo(models.Model):
    admin = models.OneToOneField(User, on_delete=models.PROTECT)
    agency_id = models.ForeignKey(Agency, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    
    class Meta:
        db_table = 'condo'
        verbose_name = "Condo"
        verbose_name_plural = "Condos"
        
    def __str__(self):
        return str(self.address)
    