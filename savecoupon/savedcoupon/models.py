from django.db import models
import uuid


class Product(models.Model):
    couponcode=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coupontitle = models.CharField(max_length=200)
    redeemed=models.BooleanField(default=False)
    saved=models.BooleanField(default=False)


