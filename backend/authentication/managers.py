from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):    
    def __create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        if not password:
            raise ValueError("The password must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_domain_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 0)

        if extra_fields.get('role') != 0:
            raise ValueError('Domain user must have role of Domain Admin')
        return self.__create_user(email, password, **extra_fields)
    
    def create_platform_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('role') != 1:
            raise ValueError('Platform user must have role of Platform Admin')
        return self.__create_user(email, password, **extra_fields)
    
    def create_agency_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 2)

        if extra_fields.get('role') != 2:
            raise ValueError('Agency user must have role of Agency Admin')
        return self.__create_user(email, password, **extra_fields)
    
    def create_condo_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 3)

        if extra_fields.get('role') != 3:
            raise ValueError('Condo user must have role of Condo Admin')
        return self.__create_user(email, password, **extra_fields)
    
    def create_comercial_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 4)

        if extra_fields.get('role') != 4:
            raise ValueError('Comercial user must have role of Comercial Admin')
        return self.__create_user(email, password, **extra_fields)
    
    def create_residence_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 5)

        if extra_fields.get('role') != 5:
            raise ValueError('Residence user must have role of Residence Admin')
        return self.__create_user(email, password, **extra_fields)
    
    def create_supervisor(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 6)

        if extra_fields.get('role') != 6:
            raise ValueError('Supervisor user must have role of Supervisor')
        return self.__create_user(email, password, **extra_fields)
    
    def create_security(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 7)

        if extra_fields.get('role') != 7:
            raise ValueError('Security user must have role of Security')
        return self.__create_user(email, password, **extra_fields)
    
    def create_resident(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 8)

        if extra_fields.get('role') != 8:
            raise ValueError('Resident user must have role of Resident')
        return self.__create_user(email, password, **extra_fields)
    
    def create_observer(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 9)

        if extra_fields.get('role') != 9:
            raise ValueError('Observer user must have role of Observer')
        return self.__create_user(email, password, **extra_fields)