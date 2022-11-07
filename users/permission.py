from rest_framework import permissions

class Vaild_request(permissions.BasePermission):
    def Allow_to_update(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True 
        
        if obj.id == request.user.id:
            return True 
        return False 
