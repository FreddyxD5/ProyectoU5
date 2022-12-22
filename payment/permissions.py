from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class CustomPermission(BasePermission):
    def has_permission(self, request, view):    
        if request.user.is_superuser:            
            return True 
        elif request.user.is_active:
            if request.method in ['GET']:
                return True
        return False

    def has_object_permission(self, request, view, obj):        
        return True



class CustomPaymentUserPermission(BasePermission):
    def has_permission(self, request, view):        
        if request.user.is_superuser:
            return True
        elif request.user.is_active:
            if request.method in ['GET','POST']:
                return True
            return False
        return False

