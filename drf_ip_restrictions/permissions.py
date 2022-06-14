from drf_ip_restrictions.settings import ip_restriction_settings
from ipware import get_client_ip


class AllowedIpList(object):
    """
    Ensure the request's IP address is on the ip white list configured in Django settings.
    """

    def has_permission(self, request, view):
        client_ip, is_routable = get_client_ip(request)

        if client_ip:
            settings = ip_restriction_settings()
            allowed_ips = settings.ALLOWED_IP_LIST
            for allowed_ip in allowed_ips:
                if client_ip == allowed_ip or client_ip.startswith(allowed_ip):
                    return True

        return False

    def has_object_permission(self, request, view, obj):
        """
        This permission class has no special implementation of per-object permissions, so the result
        will be the same as the `has_permission` method.
        """
        return self.has_permission(request, view)
