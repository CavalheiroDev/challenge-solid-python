from django.db import models
import uuid


class Products(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=150)
    price = models.IntegerField()
