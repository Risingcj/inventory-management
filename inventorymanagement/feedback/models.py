from django.db import models
from inventory.models import BusinessUnit
from django.conf import settings
from django.apps import apps

# BusinessUnit = apps.get_model(settings.inventory, 'BusinessUnit')

class Feedback(models.Model):
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.customer_name} - {self.business_unit.name}"
