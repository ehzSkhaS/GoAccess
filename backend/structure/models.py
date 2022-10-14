from django.db import models

    
class Platform(models.Model):
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(to='authentication.PlatformAdmin', related_name='platform', null=False, on_delete=models.CASCADE)
    lic = models.OneToOneField(to='control.License', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'platform'
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"
        
    def __str__(self):
        return str(self.name)


class Agency(models.Model):
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(to='authentication.AgencyAdmin', related_name='agency', null=False, on_delete=models.CASCADE)
    lic = models.OneToOneField(to='control.License', null=False, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, related_name='agency', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'agency'
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"
        
    def __str__(self):
        return str(self.name)
    
    
class Condo(models.Model):
    description = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(to='authentication.CondoAdmin', related_name='condo', on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, related_name='condo', on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    is_residential = models.BooleanField(default=False, null=False, verbose_name='residential')
    
    class Meta:
        db_table = 'condo'
        verbose_name = "Condo"
        verbose_name_plural = "Condos"
        
    def __str__(self):
        return str(self.description)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(Condo, self).save(force_insert, force_update, using, update_fields)
        
        if (self.is_residential == True):
            residential = ResidentialCondo()
            residential.condo = self
            residential.save()
        else:
            if ResidentialCondo.objects.filter(pk=self).exists():
                residential = ResidentialCondo.objects.get(pk=self)
                residential.delete()
    

class ResidentialCondo(models.Model):
    condo = models.OneToOneField(Condo, primary_key=True , on_delete=models.CASCADE)
    class Meta:
        db_table = 'residential_condo'
        verbose_name = "Residential Condo"
        verbose_name_plural = "Residential Condos"
        
    def __str__(self):
        return str(self.condo.description)


class Area(models.Model):
    name = models.CharField(max_length=255, null=False)
    max_people = models.IntegerField(verbose_name="allowed people")
    is_open = models.BooleanField(default=True, verbose_name='open')
    condo = models.ForeignKey(ResidentialCondo, related_name='area', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'area'
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        
    def __str__(self):
        return str(self.name)


class Residence(models.Model):
    description = models.CharField(max_length=255, null=False)
    number = models.IntegerField(null=False)
    street = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(to='authentication.ResidenceAdmin', related_name='residence', on_delete=models.CASCADE)
    condo = models.ForeignKey(ResidentialCondo, related_name='residence', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'residence'
        verbose_name = "Residence"
        verbose_name_plural = "Residences"
        
    def __str__(self):
        return str(self.description)
    