from django.db.models import fields
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from webscrawler.models import Data
from rest_framework.response import Response


class ValidateInfo(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ['title', 'guid', 'company', 'category', 
        'description', 'pubDate', 'updateDate']

    def validate(self, data):

        title = data["title"]
        guid = data["guid"]
        company = data["company"]
        category = data["category"]
        description = data["description"]
        pubDate = data["pubDate"]
        updateDate = data["updateDate"]

        # If GUID already is in the database return "Data already inserted" and pass
        # def validate(self, data):

        return data
    
    def save(self,data):

        item = Data()
        item.guid = data['guid']
        item.title = data['title']
        item.company = data['company']
        item.category = data['category']
        item.description = data['description']
        item.pubDate = data['pubDate']
        item.updateDate = data['updateDate']
        item.save()

        return item

