from django.db import models
from .querysets import AuditQuerySet


class AuditManager(models.Manager):
    # Custom manager that centralizes domain-level data access rules for Audit.

    #1. Avoid duplicating business rules like `is_deleted=False` across views.
    #2. Keep visibility logic (who can see which audits) out of views and serializers.
    #3. Ensure all Audit queries follow the same domain constraints by default.
    #4. Allow views to depend on high-level abstractions instead of concrete filters

    def get_queryset(self):
        return AuditQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def visible_for(self, user):
        return self.get_queryset().visible_for(user)
