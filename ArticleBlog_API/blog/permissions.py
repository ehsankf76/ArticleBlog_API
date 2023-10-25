from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied



class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Sign in as an author to be able to write an article for us.'

    def has_permission(self, request, view):
        if not request.user.is_author:
            # Allow read-only actions and comment creation
            return request.method in permissions.SAFE_METHODS
        elif request.user.is_author:
            # Allow read and write actions only on their own articles and article creation
            return request.method in ['GET', 'HEAD', 'OPTIONS', 'POST'] or view.action in ['create', 'update', 'partial_update', 'destroy']
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        if obj.author == request.user:
            return True
        
        raise PermissionDenied("Sorry! Only the writer of this article can update it.")
    

class IsAdminOrReadOnly(permissions.BasePermission):
    message = "Access Denied! :("
    def has_permission(self, request, view):
        # Allow safe methods to all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write operations only for admin users
        if request.user and request.user.is_staff:
            return True

        raise PermissionDenied("Sorry! Only admin has access to this.")