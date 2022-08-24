from django.db import models


class License(models.Model):
    LIC_STATES = (
        (1, 'Enabled'),
        (2, 'Disabled'),
    )    
    
    created = models.DateField(auto_now_add=True, null=False)
    updated = models.DateField(auto_now=True)
    end = models.DateField(null=False)
    quantity = models.IntegerField(default=5)
    state = models.PositiveSmallIntegerField(choices=LIC_STATES, null=True, default=1)
    
    class Meta:
        db_table = 'license'
        verbose_name = "License"
        verbose_name_plural = "Licenses"
        
    def __str__(self):
        return str(self.pk)


class Area(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    class Meta:
        db_table = 'area'
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        
    def __str__(self):
        return str(self.name)
    
    
class Route(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    class Meta:
        db_table = 'route'
        verbose_name = "Route"
        verbose_name_plural = "Routes"
        
    def __str__(self):
        return str(self.name)


class Round(models.Model):
    description = models.CharField(max_length=255, null=False)
    
    class Meta:
        db_table = 'round'
        verbose_name = "Round"
        verbose_name_plural = "Rounds"
        
    def __str__(self):
        return str(self.description)


