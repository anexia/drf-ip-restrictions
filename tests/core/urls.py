from django.urls import include, path
from rest_framework import routers

from testapp.views import (
    PublicInfoViewSet,
    PrivateInfoViewSet,
    PartiallyPrivateInfoViewSet,
)

router = routers.DefaultRouter()
router.register(r"public_info", PublicInfoViewSet)
router.register(r"private_info", PrivateInfoViewSet)
router.register(r"partially_private_info", PartiallyPrivateInfoViewSet)

urlpatterns = [path("api/", include(router.urls))]
