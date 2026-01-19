from rest_framework import serializers
from .models import Audit, AuditType, AuditFinding


class AuditTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditType
        fields = "__all__"

class AuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit
        fields = "__all__"
        read_only_fields = (
            "auditor",
            "created_at",
            "updated_at",
            "is_deleted",
        )

class AuditFindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditFinding
        fields = "__all__"
        read_only_fields = (
            "audit",
            "created_at",
        )

class AuditListSerializer(serializers.ModelSerializer):
    #findings = AuditFindingSerializer(many=True, read_only=True)

    class Meta:
        model = Audit
        fields = "__all__"
