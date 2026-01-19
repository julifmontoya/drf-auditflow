from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from core.permissions import (
    IsAuditor,
    IsAuditOwnerOrAdmin,
    IsAuditFindingOwnerOrAdmin,
)
from core.pagination import StandardResultsSetPagination

from .models import Audit, AuditType, AuditFinding
from .serializers import (
    AuditListSerializer,
    AuditSerializer,
    AuditTypeSerializer,
    AuditFindingSerializer,
)
from .filters import AuditFilter
from .mixins import (
    SoftDeleteMixin,
    AuditScopedQuerysetMixin,
    AuditContextMixin,
)


class AuditListProv(AuditScopedQuerysetMixin, ListAPIView):
    serializer_class = AuditListSerializer
    permission_classes = (IsAuthenticated,)


class AuditCreateProv(CreateAPIView):
    serializer_class = AuditSerializer
    permission_classes = (IsAuthenticated, IsAuditor)

    def perform_create(self, serializer):
        serializer.save(auditor=self.request.user)


class AuditDetailProv(RetrieveUpdateAPIView):
    queryset = Audit.objects.active()
    serializer_class = AuditSerializer
    permission_classes = (IsAuthenticated, IsAuditOwnerOrAdmin)
    lookup_field = "id"


class AuditDeleteProv(SoftDeleteMixin, DestroyAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = (IsAuthenticated, IsAuditOwnerOrAdmin)
    lookup_field = "id"


class AuditFindingListCreateProv(AuditContextMixin, ListCreateAPIView):
    serializer_class = AuditFindingSerializer
    permission_classes = (IsAuthenticated, IsAuditOwnerOrAdmin)

    def get_queryset(self):
        return AuditFinding.objects.filter(audit=self.get_audit())

    def perform_create(self, serializer):
        serializer.save(audit=self.get_audit())


class AuditFindingDetailProv(RetrieveUpdateAPIView):
    queryset = AuditFinding.objects.select_related("audit", "audit__auditor")
    serializer_class = AuditFindingSerializer
    permission_classes = (IsAuthenticated, IsAuditFindingOwnerOrAdmin)
    lookup_field = "id"


class AuditList(ListAPIView):
    queryset = Audit.objects.active()
    serializer_class = AuditListSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AuditFilter
    pagination_class = StandardResultsSetPagination


class AuditDetail(RetrieveAPIView):
    queryset = Audit.objects.active()
    serializer_class = AuditSerializer
    permission_classes = (AllowAny,)
    lookup_field = "id"


class AuditTypeList(ListAPIView):
    queryset = AuditType.objects.all()
    serializer_class = AuditTypeSerializer
    permission_classes = (AllowAny,)
