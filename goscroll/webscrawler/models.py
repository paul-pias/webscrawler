from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# * title
# * GUID
# * Company
# * Categories (multiple)
# * description
# * Timestamps

class Data(models.Model):

    title = models.CharField(max_length = 300)
    guid = models.IntegerField()
    company = models.CharField(max_length = 50)
    category = models.JSONField()
    description = models.CharField(max_length = 5000)
    pubDate = models.CharField(max_length = 50)
    updateDate = models.CharField(max_length = 50)

    def __str__(self):
        return self.guid
