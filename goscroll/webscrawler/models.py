# from typing_extensions import Required
from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# * title
# * GUID
# * Company
# * Categories (multiple) ['python', 'scala', 'reactjs] 
# * description
# * Timestamps

class Category(models.Model):
    """
        Make a  seperate table for types of jobs
    """

    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name


class Data(models.Model):
    """
        Database columns for job query. 
    """

    title = models.CharField(max_length = 300)
    guid = models.IntegerField(primary_key = True)
    company = models.CharField(max_length = 50)
    # category = models.CharField(max_length = 50)
    categories = models.ManyToManyField(Category, related_name= 'datas', blank= True) 
    description = models.CharField(max_length = 5000)
    pubDate = models.CharField(max_length = 50)  ## DateTimeParser
    updateDate = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.guid)
