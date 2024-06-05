from rest_framework.permissions import BasePermission

class IsHRManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_hr_manager

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_employee
