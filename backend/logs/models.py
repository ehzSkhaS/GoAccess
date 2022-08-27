from django.db import models
from django.utils import timezone


class Alert(models.Model):
    description = models.CharField(max_length=255, null=False)
    created_date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'alert'
        verbose_name = "Alert"
        verbose_name_plural = "Alerts"
        
    def __str__(self):
        return str(self.description)

