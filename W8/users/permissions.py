from rest_framework import permissions


class LocalOrIsAuthenticatedPermission(permissions.IsAuthenticated):
    """
    Local Have Permission already
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        if ip_addr == '127.0.0.1':
            return True
        return super().has_permission(request, view)
