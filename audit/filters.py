import django_filters
from .models import Audit

class AuditFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name="status")
    audit_type = django_filters.NumberFilter(field_name="audit_type")

    class Meta:
        model = Audit
        fields = ["status", "audit_type"]
