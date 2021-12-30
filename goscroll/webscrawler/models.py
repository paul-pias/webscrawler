# from typing_extensions import Required
from django.db import models

class Data(models.Model):
    """
        # Model FIelds
            * title
            * GUID
            * Company
            * Categories (multiple) eg. ('python', 'scala', 'reactjs) 
            * description
            * Timestamps 
    """

    title = models.CharField(max_length = 300)
    guid = models.IntegerField(primary_key = True, name = 'guid')
    company = models.CharField(max_length = 50)
    categories = models.CharField(max_length = 50)
    description = models.CharField(max_length = 5000)
    pubDate = models.DateTimeField() 
    updated = models.DateTimeField()

    def __str__(self):
        return str(self.guid)
