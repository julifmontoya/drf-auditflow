from django.contrib import admin
from. models import AuditType
from. models import Audit
from. models import AuditFinding

admin.site.register(AuditType)
admin.site.register(Audit)
admin.site.register(AuditFinding)