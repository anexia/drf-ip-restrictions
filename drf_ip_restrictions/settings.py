from django.conf import settings
from rest_framework.settings import APISettings

__all__ = ["ip_restriction_settings"]


DRF_IP_RESTRICTION_SETTINGS = {
    "ALLOWED_IP_LIST": [],
}


def ip_restriction_settings():
    return APISettings(
        user_settings=getattr(settings, "DRF_IP_RESTRICTION_SETTINGS", {}),
        defaults=DRF_IP_RESTRICTION_SETTINGS,
    )
