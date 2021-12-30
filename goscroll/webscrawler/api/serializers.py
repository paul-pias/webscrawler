from rest_framework import serializers
from rest_framework.authtoken.models import Token
from webscrawler.models import Data
from rest_framework.response import Response


class ValidateInfo(serializers.ModelSerializer):
    # categories = serializers.ListField(child = serializers.CharField())
    class Meta:
        model = Data
        fields = '__all__'
    
    def create(self, validated_data):
        
        data_object = Data.objects.create(**validated_data)

        return data_object


class GetInfo(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = '__all__'
    
    # def update(self, instance, validated_data):

    #     data_object = Data.objects.update_or_create(**validated_data)

    #     print(data_object)

class BulkEntry(serializers.Serializer):

    inputs = ValidateInfo(many =True)

    