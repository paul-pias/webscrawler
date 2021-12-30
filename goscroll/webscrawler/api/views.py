from django.http.response import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from webscrawler.api.serializers import (

    ValidateInfo,
    BulkEntry,
)
from rest_framework.decorators import api_view
from webscrawler.models import Data
from utils.scrawler import WebScrapper
from .serializers import  GetInfo
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


##Initial Entry

def initial_entry(request):
    """
    Get initial data from scrapping into a dictionary and pushes to DB
    
    Parameters:
        url (string) = A string containing a url                                         eg. ["","","", ""]                               ## 

    Returns:
            HttpResponse
    """


    url = "https://stackoverflow.com/jobs/feed"
    get_all_feed = WebScrapper(url = url).get_data()
    for key, value in get_all_feed.items():
        if Data.objects.filter(guid = key).exists():
            continue
        value['guid'] = key
        value['categories'] = ",".join(str(category) for category in value['categories'] )
        
        serializer = ValidateInfo(data = value)
        
        if serializer.is_valid():
            serializer.save()
    return HttpResponse("Success")


## Bulk Entry
@swagger_auto_schema(methods= ['POST'], request_body= BulkEntry )
@api_view(['POST'])
def bulk_entry(request):

    """
    Returns a HTTPResponse
    Parameters:

        jsonData (list) = List of list contains nested dictionaries         eg. [{}, {}, {}, {}, {}, {}, {}]     
        
    Returns:
            HttpResponse
    """
    
    if request.method == 'POST':
        bulk_data = request.data.get("inputs", [])
        print(bulk_data)
        for data in bulk_data:
            value = data.get('guid')
            if Data.objects.filter(guid = int(value)).exists():
                continue
            serializer = ValidateInfo(data = data)
            if serializer.is_valid():
                serializer.save()
    return HttpResponse("Success")


class JobViewSet(ModelViewSet):
    """
        Responsible to make Create, Retrieve(List, Detail), PUT, PATCH operation

    """
    queryset = Data.objects.all()
    serializer_class = GetInfo

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('guid', openapi.IN_QUERY, description="search with guid", type=openapi.TYPE_INTEGER),
        openapi.Parameter('company', openapi.IN_QUERY, description="search with company", type=openapi.TYPE_STRING),
        openapi.Parameter('categories', openapi.IN_QUERY, description="search with job type", type=openapi.TYPE_STRING)
        ])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        guid = request.query_params.get('guid')
        if guid:
            queryset = queryset.filter(guid=guid)
        
        company_name = request.query_params.get('company')
        if company_name:
            queryset = queryset.filter(company__icontains=company_name)
        
        job_type = request.query_params.get('company')
        if job_type is not None:
            queryset = queryset.filter(categories__icontains=company_name)
        

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(operation_description="partial_update description override")
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)




##Create           Default Serializer




##Update           Default Serializer

##Delete

##PUT

##PATCH             Default Serializer

##BULK Entry