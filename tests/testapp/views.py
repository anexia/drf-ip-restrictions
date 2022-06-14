from drf_ip_restrictions import AllowedIpList
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PublicInfo, PrivateInfo, PartiallyPrivateInfo
from .serializers import PublicInfoSerializer, PrivateInfoSerializer, PartiallyPrivateInfoSerializer


class PublicInfoViewSet(viewsets.ModelViewSet):
    queryset = PublicInfo.objects.all()
    serializer_class = PublicInfoSerializer


class PrivateInfoViewSet(viewsets.ModelViewSet):
    queryset = PrivateInfo.objects.all()
    serializer_class = PrivateInfoSerializer
    permission_classes = (AllowedIpList, )


class PartiallyPrivateInfoViewSet(viewsets.ModelViewSet):
    queryset = PartiallyPrivateInfo.objects.all()
    serializer_class = PartiallyPrivateInfoSerializer

    @action(
        detail=False,
        methods=["get"],
        http_method_names=["get"],
        authentication_classes=[],
        permission_classes=[AllowedIpList],
        url_path=r"private-insight",
    )
    def private_insight(self, request, *args, **kwargs):
        return Response(status=200, data={'Test': 'OK'})
