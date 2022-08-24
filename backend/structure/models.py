from django.db import models

    
class Platform(models.Model):
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(to='authentication.PlatformAdmin', null=False, on_delete=models.CASCADE)
    lic = models.OneToOneField(to='control.License', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'platform'
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"
        
    def __str__(self):
        return str(self.name)


class Agency(models.Model):
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(to='authentication.AgencyAdmin', null=False, on_delete=models.CASCADE)
    lic = models.OneToOneField(to='control.License', null=False, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'agency'
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"
        
    def __str__(self):
        return str(self.name)
    
    
class Condo(models.Model):
    description = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(to='authentication.CondoAdmin', on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    
    class Meta:
        abstract = True
        db_table = 'condo'
        verbose_name = "Condo"
        verbose_name_plural = "Condos"
        
    def __str__(self):
        return str(self.description)


class ResidencialCondo(Condo):
    class Meta:
        db_table = 'residencial_condo'
        verbose_name = "Residencial Condo"
        verbose_name_plural = "Residencial Condos"
        
    def __str__(self):
        return str(self.description)


class CommercialCondo(Condo):
    class Meta:
        db_table = 'commercial_condo'
        verbose_name = "Commercial Condo"
        verbose_name_plural = "Commercial Condos"
        
    def __str__(self):
        return str(self.description)


class Residence(models.Model):
    description = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(to='authentication.ResidenceAdmin', on_delete=models.CASCADE)
    condo = models.ForeignKey(ResidencialCondo, on_delete=models.CASCADE)
    number = models.IntegerField(null=False)
    street = models.CharField(max_length=255, null=True)
    
    class Meta:
        db_table = 'residence'
        verbose_name = "Residence"
        verbose_name_plural = "Residences"
        
    def __str__(self):
        return str(self.description)
    