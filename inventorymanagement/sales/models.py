from django.db import models
from django.conf import settings
from django.apps import apps
from inventory.models import BusinessUnit
# Assuming 'inventory' is the correct app name and it's properly installed
# BusinessUnit = apps.get_model(settings.inventory, 'BusinessUnit')

class Sales(models.Model):
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
