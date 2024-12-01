from django.db import models
from django.conf import settings
from django.apps import apps
from authentication.models import User

# User = apps.get_model(settings.authentication, 'User')


class BusinessUnit(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)


class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    stock_level = models.IntegerField()
    reorder_threshold = models.IntegerField()
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE)
