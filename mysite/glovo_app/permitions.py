from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.IsAdminUser and request.user.role == 'owner'

class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'client'

class IsCourier(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.IsAuthenticatedOrReadOnly and request.user.role == 'courier'
