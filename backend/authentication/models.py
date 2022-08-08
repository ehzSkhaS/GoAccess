import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    
    # DOMAIN_ADMIN = 0
    # PLATFORM_ADMIN = 1
    # AGENCY_ADMIN =2
    # CONDO_ADMIN = 3
    # COMMERCIAL_ADMIN = 4
    # RESIDENCE_ADMIN = 5
    # SUPERVISOR = 6
    # SECURITY = 7
    # RESIDENT = 8
    # OBSERVER = 9
    
    # ROLE_CHOICES = (
    #     (DOMAIN_ADMIN, 'Domain'),
    #     (PLATFORM_ADMIN, 'Platform'),
    #     (AGENCY_ADMIN, 'Agency'),
    #     (CONDO_ADMIN, 'Condo'),
    #     (COMMERCIAL_ADMIN, 'Commercial'),
    #     (RESIDENCE_ADMIN, 'Residence'),
    #     (SUPERVISOR, 'Supervisor'),
    #     (SECURITY, 'Security'),
    #     (RESIDENT, 'Resident'),
    #     (OBSERVER, 'Observer'),
    # )
    
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=255, blank=True)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=9)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'user'
    
    def __str__(self):
        return str(self.email)

