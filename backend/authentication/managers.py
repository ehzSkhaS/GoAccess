from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, email, password, **extra_fields):
        values = [email, ]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
"""     
    def create_platform_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('role') != 1:
            raise ValueError('Platform user must have role of Platform Admin')
        return self.create_user(email, password, **extra_fields)
    
    def create_agency_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 2)

        if extra_fields.get('role') != 2:
            raise ValueError('Agency user must have role of Agency Admin')
        return self.create_user(email, password, **extra_fields)
    
    def create_condo_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 3)

        if extra_fields.get('role') != 3:
            raise ValueError('Condo user must have role of Condo Admin')
        return self.create_user(email, password, **extra_fields)
    
    def create_comercial_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 4)

        if extra_fields.get('role') != 4:
            raise ValueError('Commercial user must have role of Commercial Admin')
        return self.create_user(email, password, **extra_fields)
    
    def create_residence_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 5)

        if extra_fields.get('role') != 5:
            raise ValueError('Residence user must have role of Residence Admin')
        return self.create_user(email, password, **extra_fields)
    
    def create_supervisor(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 6)

        if extra_fields.get('role') != 6:
            raise ValueError('Supervisor user must have role of Supervisor')
        return self.create_user(email, password, **extra_fields)
    
    def create_security(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 7)

        if extra_fields.get('role') != 7:
            raise ValueError('Security user must have role of Security')
        return self.create_user(email, password, **extra_fields)
    
    def create_resident(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 8)

        if extra_fields.get('role') != 8:
            raise ValueError('Resident user must have role of Resident')
        return self.create_user(email, password, **extra_fields)
    
    def create_observer(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 9)

        if extra_fields.get('role') != 9:
            raise ValueError('Observer user must have role of Observer')
        return self.create_user(email, password, **extra_fields) 
"""