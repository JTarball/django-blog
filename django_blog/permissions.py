'''
    django_blog.permissions
    =======================

    Blog Custom Permissions for REST API
'''
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet
        return request.user.is_staff or request.user.is_superuser
