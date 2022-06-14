from rest_framework import serializers

from testapp.models import PublicInfo, PrivateInfo, PartiallyPrivateInfo


class PublicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicInfo
        fields = ['name']


class PrivateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateInfo
        fields = ['name']


class PartiallyPrivateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartiallyPrivateInfo
        fields = ['name']
