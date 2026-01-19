from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.urls import re_path
from . import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/affiliate/', include('user.urls')),
    path('v1/', include('audit.urls')),
    path('', views.apiMsg)
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]

# Swagger / OpenAPI
urlpatterns += [
    path("v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("v1/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
