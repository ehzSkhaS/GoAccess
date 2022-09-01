from django.db import models
from django.utils import timezone


class Alert(models.Model):
    PENDING = 0
    NOT_SEEN = 1
    ATTENDED = 2
    
    CHOICES = (
        (PENDING, 'Pending'),
        (NOT_SEEN, 'Not Seen'),
        (ATTENDED, 'Attended'),
    )
    
    description = models.CharField(max_length=255)
    state = models.PositiveSmallIntegerField(choices=CHOICES, null=True, default=0)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    user = models.ForeignKey(to='authentication.Resident', null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'alert'
        verbose_name = "Alert"
        verbose_name_plural = "Alerts"
        
    def __str__(self):
        return str(self.description)


class ReceivedAlert(models.Model):
    description = models.CharField(max_length=255)
    attended_date = models.DateTimeField(default=timezone.now, editable=False)
    user = models.ForeignKey(to='authentication.Security', null=False, on_delete=models.CASCADE)
    alert = models.ForeignKey(Alert, null=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'received_alert'
        verbose_name = "Received Alert"
        verbose_name_plural = "Received Alerts"
        
    def __str__(self):
        return str(self.description)

