from rest_framework.exceptions import PermissionDenied

def has_permission(provider_user, user):
    if provider_user != user and not user.is_superuser:
            raise PermissionDenied()