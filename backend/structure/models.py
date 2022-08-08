from django.db import models

from authentication.models import *

    
class License(models.Model):
    LIC_STATES = (
        (1, 'Enabled'),
        (2, 'Disabled'),
    )    
    
    created = models.DateField(auto_now_add=True, null=False)
    udated = models.DateField(auto_now=True)
    ended = models.DateField(null=False)
    quantity = models.IntegerField(default=5)
    licstate = models.PositiveSmallIntegerField(choices=LIC_STATES, null=True, default=1)
    
    class Meta:
        db_table = 'license'
        verbose_name = "License"
        verbose_name_plural = "Licenses"
        
    def __str__(self):
        return str(self.ended)


class Platform(models.Model):
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    lic = models.OneToOneField(License, null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'platform'
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"
        
    def __str__(self):
        return str(self.name)


class Agency(models.Model):
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    lic = models.OneToOneField(License, null=False, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'agency'
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"
        
    def __str__(self):
        return str(self.name)
    
    
class Condo(models.Model):
    description = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    
    class Meta:
        db_table = 'condo'
        verbose_name = "Condo"
        verbose_name_plural = "Condos"
        
    def __str__(self):
        return str(self.description)
    

class Residence(models.Model):
    description = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
    number = models.IntegerField(null=False)
    street = models.CharField(max_length=255, null=True)
    
    class Meta:
        db_table = 'residence'
        verbose_name = "Residence"
        verbose_name_plural = "Residences"
        
    def __str__(self):
        return str(self.description)
    