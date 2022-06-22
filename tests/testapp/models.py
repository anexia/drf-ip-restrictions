from django.db import models


class PublicInfo(models.Model):
    """
    Public info without IP restrictions.
    """

    name = models.CharField(max_length=50, primary_key=True)


class PrivateInfo(models.Model):
    """
    Private info with IP restrictions for all endpoints.
    """

    name = models.CharField(max_length=50, primary_key=True)


class PartiallyPrivateInfo(models.Model):
    """
    Partially private info with IP restrictions for single GET endpoint 'private-insight'.
    """

    name = models.CharField(max_length=50, primary_key=True)
