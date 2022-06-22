from unittest.mock import patch

from django.test import TestCase, override_settings
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_403_FORBIDDEN,
)

from testapp.models import PublicInfo, PrivateInfo, PartiallyPrivateInfo


class TestApi(TestCase):
    def setUp(self):
        super().setUp()

        self.public_info = PublicInfo.objects.create(name="public1")
        self.private_info = PrivateInfo.objects.create(name="private1")
        self.partially_private_info = PartiallyPrivateInfo.objects.create(
            name="partially_private1"
        )

    def assert_public_response(self, response, expected_name):
        # check response
        self.assertEqual(HTTP_200_OK, response.status_code, response.content)
        response_data = response.json()
        self.assertEqual(1, len(response_data))
        self.assertEqual(expected_name, response_data[0]["name"])

    def test_get_public_info_internally(self):
        """Assert private view set is accessible from valid IP"""
        response = self.client.get(path=f"/api/public_info/")
        self.assert_public_response(response, "public1")

    @override_settings(
        DRF_IP_RESTRICTION_SETTINGS={"ALLOWED_IP_LIST": ["200.200.200.200"]}
    )
    def test_get_public_info_externally(self):
        """Assert private view set is accessible from invalid IP"""
        response = self.client.get(path=f"/api/public_info/")
        self.assert_public_response(response, "public1")

    def test_get_private_info_internally(self):
        """Assert private view set is accessible from valid IP"""
        response = self.client.get(path=f"/api/private_info/")
        self.assertEqual(HTTP_200_OK, response.status_code, response.content)
        response_data = response.json()
        self.assertEqual(1, len(response_data))
        self.assertEqual("private1", response_data[0]["name"])

    @override_settings(
        DRF_IP_RESTRICTION_SETTINGS={"ALLOWED_IP_LIST": ["200.200.200.200"]}
    )
    def test_get_restricted_private_info_internally(self):
        """Assert private endpoint from public view set is not accessible from invalid IP"""
        response = self.client.get(path=f"/api/private_info/")
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_get_partially_private_info_internally(self):
        """Assert public endpoint from public view set is accessible from valid IP"""
        response = self.client.get(path=f"/api/partially_private_info/")
        self.assert_public_response(response, "partially_private1")

    @override_settings(
        DRF_IP_RESTRICTION_SETTINGS={"ALLOWED_IP_LIST": ["200.200.200.200"]}
    )
    def test_get_partially_private_info_externally(self):
        """Assert public endpoint from public view set is accessible from invalid IP"""
        response = self.client.get(path=f"/api/partially_private_info/")
        self.assert_public_response(response, "partially_private1")

    def test_get_restricted_partially_private_info_internally(self):
        """Assert private endpoint from public view set is accessible from valid IP"""
        response = self.client.get(path=f"/api/partially_private_info/private-insight/")
        self.assertEqual(HTTP_200_OK, response.status_code, response.content)

        # check response
        response_data = response.json()
        self.assertEqual(1, len(response_data))
        self.assertEqual("OK", response_data["Test"])

    @override_settings(
        DRF_IP_RESTRICTION_SETTINGS={"ALLOWED_IP_LIST": ["200.200.200.200"]}
    )
    def test_get_restricted_partially_private_info_internally(self):
        """Assert private endpoint from public view set is not accessible from invalid IP"""
        response = self.client.get(path=f"/api/partially_private_info/private-insight/")
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_get_restricted_private_info_detail_internally(self):
        response = self.client.get(path=f"/api/private_info/{self.private_info.pk}/")
        self.assertEqual(response.status_code, HTTP_200_OK)

    @override_settings(
        DRF_IP_RESTRICTION_SETTINGS={"ALLOWED_IP_LIST": ["200.200.200.200"]}
    )
    def test_get_restricted_private_info_detail_externally(self):
        response = self.client.get(path=f"/api/private_info/{self.private_info.pk}/")
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    @patch("drf_ip_restrictions.permissions.get_client_ip", side_effect=[(None, None)])
    def test_get_restricted_private_with_no_ip_address(self, mock):
        """Assert private endpoint from public view set is not accessible when IP does not exist"""
        response = self.client.get(path=f"/api/private_info/")
        self.assertEqual(mock.call_count, 1)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
