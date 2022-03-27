from django.conf import settings
from django.db import models

from skymarket.users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=200, null=True)
    price = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True)
    description = models.CharField(max_length=1000, null=True)


class Comment(models.Model):
    text = models.CharField(max_length=1000, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
