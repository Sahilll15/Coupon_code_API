
from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    isValid=models.BooleanField(True)
    expiration_date = models.DateField()

    def __str__(self):
        return self.code
