from django.apps import apps
from django.conf import settings
from django.test import SimpleTestCase

from testapp.models import PublicInfo, PrivateInfo, PartiallyPrivateInfo


class TestSetup(SimpleTestCase):
    def test_installed_apps(self):
        self.assertIn("drf_ip_restrictions", settings.INSTALLED_APPS)

    def test_models(self):
        self.assertIs(apps.get_model("testapp", "PublicInfo"), PublicInfo)
        self.assertIs(apps.get_model("testapp", "PrivateInfo"), PrivateInfo)
        self.assertIs(
            apps.get_model("testapp", "PartiallyPrivateInfo"), PartiallyPrivateInfo
        )
