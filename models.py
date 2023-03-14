from django.db import models
from django.utils import timezone


class Customer(models.Model):
    # cust_id=models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='products')
def is_inactive(self):
        two_months_ago = timezone.now() - timezone.timedelta(days=60)
        return self.created_at <= two_months_ago
