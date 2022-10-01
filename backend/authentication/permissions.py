from rest_framework import permissions


class IsCurrentUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True

  
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user


class IsCurrentSuperUser(permissions.BasePermission):
    message = 'You are not superuser'
    
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
    

class PlatformAdminPerms(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if view.action in ['list', 'create', 'destroy']:
            return request.user.is_superuser
        # if view.action in ['retrieve', 'update', 'partial_update']:
        #     return request.user.is_superuser or 
            

"""
class IsCurrentUserPlatformAdmin(permissions.BasePermission):
    message = 'You are not the platform admin'
    
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_authenticated and request.user.role == 1):
            return True


class IsCurrentUserAgencyAdmin(permissions.BasePermission):
    message = 'You are not the agency admin'
    
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_authenticated and request.user.role == 2):
            return True


class IsCurrentUserCondoAdmin(permissions.BasePermission):
    message = 'You are not the condo admin'
    
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_authenticated and request.user.role == 3):
            return True


class IsCurrentUserCommercialAdmin(permissions.BasePermission):
    message = 'You are not the commercial admin'
    
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_authenticated and request.user.role == 4):
            return True


class IsCurrentUserResidenceAdmin(permissions.BasePermission):
    message = 'You are not the residence admin'
    
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_authenticated and request.user.role == 5):
            return True


class IsCurrentUserSupervisor(permissions.BasePermission):
    message = 'You are not a supervisor'
    
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_authenticated and request.user.role == 6):
            return True


class IsCurrentUserSecurity(permissions.BasePermission):
    message = 'You are not a security member'
    
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_authenticated and request.user.role == 7):
            return True 


class IsCurrentUserResident(permissions.BasePermission):
    message = 'You are not a resident'
    
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_authenticated and request.user.role == 8):
            return True


class IsCurrentUserObserver(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_authenticated and request.user.role == 9):
            return True 
"""