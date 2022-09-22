import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='public identifier')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='active')
    is_resident = models.BooleanField(default=False, verbose_name='resident')
    is_security = models.BooleanField(default=False, verbose_name='security')
    is_supervisor = models.BooleanField(default=False, verbose_name='supervisor')
    is_residenceadmin = models.BooleanField(default=False, verbose_name='residence admin')
    is_condoadmin = models.BooleanField(default=False, verbose_name='condo admin')
    is_agencyadmin = models.BooleanField(default=False, verbose_name='agency admin')
    is_platformadmin = models.BooleanField(default=False, verbose_name='platform admin')
    is_staff = models.BooleanField(default=False, verbose_name='staff')
    is_superuser = models.BooleanField(default=False, verbose_name='superuser')
    last_login = models.DateTimeField(blank=True, null=True, editable=False, verbose_name='last login')
    created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name='created date')
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'user'
        
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(User, self).save(force_insert, force_update, using, update_fields)
        
        if (self.is_resident == True):
            resident = Resident()
            resident.user = self
            resident.save()
        else:
            if Resident.objects.filter(pk=self).exists():
                resident = Resident.objects.get(pk=self)
                resident.delete()
                
        if (self.is_security == True):
            security = Security()
            security.user = self
            security.save()
        else:
            if Security.objects.filter(pk=self).exists():
                security = Security.objects.get(pk=self)
                security.delete()
        
        if (self.is_supervisor == True):
            supervisor = Supervisor()
            supervisor.user = self
            supervisor.save()
        else:
            if Supervisor.objects.filter(pk=self).exists():
                supervisor = Supervisor.objects.get(pk=self)
                supervisor.delete()
        
        if (self.is_residenceadmin == True):
            admin = ResidenceAdmin()
            admin.user = self
            admin.save()
        else:
            if ResidenceAdmin.objects.filter(pk=self).exists():
                admin = ResidenceAdmin.objects.get(pk=self)
                admin.delete()
        
        if (self.is_condoadmin == True):
            admin = CondoAdmin()
            admin.user = self
            admin.save()
        else:
            if CondoAdmin.objects.filter(pk=self).exists():
                admin = CondoAdmin.objects.get(pk=self)
                admin.delete()
        
        if (self.is_agencyadmin == True):
            admin = AgencyAdmin()
            admin.user = self
            admin.save()
        else:
            if AgencyAdmin.objects.filter(pk=self).exists():
                admin = AgencyAdmin.objects.get(pk=self)
                admin.delete()
        
        if (self.is_platformadmin == True):
            admin = PlatformAdmin()
            admin.user = self
            admin.save()
        else:
            if PlatformAdmin.objects.filter(pk=self).exists():
                admin = PlatformAdmin.objects.get(pk=self)
                admin.delete()
        
    def __str__(self):
        return str(self.email)


class Resident(models.Model):
    user = models.OneToOneField(User, primary_key=True , on_delete=models.CASCADE)
    residence = models.ForeignKey(to='structure.Residence', null=True, on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'resident'
        verbose_name = "Resident"
        verbose_name_plural = "Residents"
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if (self.user.is_resident == False):
            self.user.is_resident = True
            self.user.save()
        super(Resident, self).save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        if (self.user.is_resident == True):
            self.user.is_resident = False
            self.user.save()
        super(Resident, self).delete(using, keep_parents)
        
    def __str__(self):
        return str(self.user.email)


class Security(models.Model):
    user = models.OneToOneField(User, primary_key=True , on_delete=models.CASCADE)
    agency = models.ForeignKey(to='structure.Agency', null=True, on_delete=models.DO_NOTHING)
        
    class Meta:
        db_table = 'security'
        verbose_name = "Security"
        verbose_name_plural = "Securities"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if (self.user.is_security == False):
            self.user.is_security = True
            self.user.save()
        super(Security, self).save(force_insert, force_update, using, update_fields)
        
    def delete(self, using=None, keep_parents=False):
        if (self.user.is_security == True):
            self.user.is_security = False
            self.user.save()
        super(Security, self).delete(using, keep_parents)

    def __str__(self):
        return str(self.user.email)
        
        
class Supervisor(models.Model):
    user = models.OneToOneField(User, primary_key=True , on_delete=models.CASCADE)
    agency = models.ForeignKey(to='structure.Agency', null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'supervisor'
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisors"
        
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if (self.user.is_supervisor == False):
            self.user.is_supervisor = True
            self.user.save()
        super(Supervisor, self).save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        if (self.user.is_supervisor == True):
            self.user.is_supervisor = False
            self.user.save()
        super(Supervisor, self).delete(using, keep_parents)

    def __str__(self):
        return str(self.user.email)


class ResidenceAdmin(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'residence_admin'
        verbose_name = "Residence Admin"
        verbose_name_plural = "Residence Admins"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if (self.user.is_residenceadmin == False):
            self.user.is_residenceadmin = True
            self.user.save()
        super(ResidenceAdmin, self).save(force_insert, force_update, using, update_fields)
        
    def delete(self, using=None, keep_parents=False):
        if (self.user.is_residenceadmin == True):
            self.user.is_residenceadmin = False
            self.user.save()
        super(ResidenceAdmin, self).delete(using, keep_parents)
    
    def __str__(self):
        return str(self.user.email)


class CondoAdmin(models.Model):
    user = models.OneToOneField(User, primary_key=True , on_delete=models.CASCADE)
    
    class Meta:
            db_table = 'condo_admin'
            verbose_name = "Condo Admin"
            verbose_name_plural = "Condo Admins"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if (self.user.is_condoadmin == False):
            self.user.is_condoadmin = True
            self.user.save()
        super(CondoAdmin, self).save(force_insert, force_update, using, update_fields)
        
    def delete(self, using=None, keep_parents=False):
        if (self.user.is_condoadmin == True):
            self.user.is_condoadmin = False
            self.user.save()
        super(CondoAdmin, self).delete(using, keep_parents)
        
    def __str__(self):
        return str(self.user.email)


class AgencyAdmin(models.Model):
    user = models.OneToOneField(User, primary_key=True , on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'agency_admin'
        verbose_name = "Agency Admin"
        verbose_name_plural = "Agency Admins"
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if (self.user.is_agencyadmin == False):
            self.user.is_agencyadmin = True
            self.user.save()
        super(AgencyAdmin, self).save(force_insert, force_update, using, update_fields)
        
    def delete(self, using=None, keep_parents=False):
        if (self.user.is_agencyadmin == True):
            self.user.is_agencyadmin = False
            self.user.save()
        super(AgencyAdmin, self).delete(using, keep_parents)
        
    def __str__(self):
        return str(self.user.email)


class PlatformAdmin(models.Model):
    user = models.OneToOneField(User, primary_key=True , on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'platform_admin'
        verbose_name = "Platform Admin"
        verbose_name_plural = "Platform Admins"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if (self.user.is_platformadmin == False):
            self.user.is_platformadmin = True
            self.user.save()
        super(PlatformAdmin, self).save(force_insert, force_update, using, update_fields)
        
    def delete(self, using=None, keep_parents=False):
        if (self.user.is_platformadmin == True):
            self.user.is_platformadmin = False
            self.user.save()
        super(PlatformAdmin, self).delete(using, keep_parents)
    
    def __str__(self):
        return str(self.user.email)

