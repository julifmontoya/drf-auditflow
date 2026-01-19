from rest_framework.permissions import BasePermission


class IsAuditor(BasePermission):
    """
    Allows access to authenticated non-admin users.
    Must be used together with IsAuthenticated.
    """

    def has_permission(self, request, view):
        return not request.user.is_superuser


class IsAuditOwnerOrAdmin(BasePermission):
    """
    Object-level permission for Audit
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.auditor == request.user


class IsAuditFindingOwnerOrAdmin(BasePermission):
    """
    Object-level permission for AuditFinding
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.audit.auditor == request.user
