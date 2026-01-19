from django.urls import path
from .views import (
    AuditList,
    AuditDetail,
    AuditTypeList,
    AuditListProv,
    AuditCreateProv,
    AuditDetailProv,
    AuditDeleteProv,
    AuditFindingListCreateProv,
    AuditFindingDetailProv,    
)

urlpatterns = [
    path("audits/", AuditList.as_view()),
    path("audits/<id>/", AuditDetail.as_view()),
    path("audit-types/", AuditTypeList.as_view()),
    path("provider/audits/", AuditListProv.as_view()),
    path("provider/audits/create/", AuditCreateProv.as_view()),
    path("provider/audits/<id>/", AuditDetailProv.as_view()),
    path("provider/audits/<id>/delete/", AuditDeleteProv.as_view()),
    path("provider/audits/<int:audit_id>/findings/",
         AuditFindingListCreateProv.as_view()),
    path("provider/audit-findings/<int:id>/",
         AuditFindingDetailProv.as_view()),
]
