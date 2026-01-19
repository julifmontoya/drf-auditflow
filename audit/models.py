from django.db import models
from .managers import AuditManager
from user.models import User


class AuditType(models.Model):
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name


class Audit(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_COMPLETED = "completed"

    STATUS_CHOICES = (
        (STATUS_DRAFT, "Draft"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_COMPLETED, "Completed"),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    auditor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="audits")
    audit_type = models.ForeignKey(AuditType, on_delete=models.SET_NULL, null=True, related_name="audits")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuditManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class AuditFinding(models.Model):
    SEVERITY_LOW = "low"
    SEVERITY_MEDIUM = "medium"
    SEVERITY_HIGH = "high"

    SEVERITY_CHOICES = (
        (SEVERITY_LOW, "Low"),
        (SEVERITY_MEDIUM, "Medium"),
        (SEVERITY_HIGH, "High"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    evidence = models.JSONField(null=True, blank=True)
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE, related_name="findings")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.severity})"
