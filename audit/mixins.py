from django.shortcuts import get_object_or_404
from .models import Audit

# Reusable view mixins for Audit-related APIs

class SoftDeleteMixin:
    """
    Replaces hard delete with soft delete
    """

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save(update_fields=["is_deleted"])

class AuditScopedQuerysetMixin:
    """
    Restricts Audit queryset based on user role
    Superuser -> all active audits
    Auditor    -> own active audits
    """

    def get_queryset(self):
        return Audit.objects.visible_for(self.request.user)

class AuditContextMixin:
    """
    Loads Audit from URL and enforces object permissions.
    Used for nested resources like AuditFinding.
    """

    def get_audit(self):
        audit = get_object_or_404(
            Audit.objects.active(),
            id=self.kwargs["audit_id"]
        )
        self.check_object_permissions(self.request, audit)
        return audit
