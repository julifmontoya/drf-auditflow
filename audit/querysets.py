from django.db import models


class AuditQuerySet(models.QuerySet):
    # Centralizes Audit data rules so they are not duplicated across views, managers, or services.
    # - Define what an "active" Audit means in the system.
    # - Define visibility rules based on the requesting user.

    def active(self):
        return self.filter(is_deleted=False)

    def visible_for(self, user):
        if user.is_superuser:
            return self.active()
        return self.active().filter(auditor=user)
