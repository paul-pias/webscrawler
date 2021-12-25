from requests.api import get, post
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from webscrawler.api.serializers import (

    ValidateInfo,
)

from goscroll.utils.scrawler import WebScrapper
import requests

##Initial Entry


    
            



@api_view(['GET'],)
@permission_classes([AllowAny])
def initial_entry(request):
    print("Inside the function")

    get_all_feed = WebScrapper("https://stackoverflow.com/jobs/feed").get_data()
    data = {}
    if request.method == 'GET':
        print("Inside Post method")
        for key, value in get_all_feed.items():
            data['guid'] = key
            data['title'] = get_all_feed[key]['title']
            data['company'] = get_all_feed[key]['company']
            data['category'] = get_all_feed[key]['category']
            data['description'] = get_all_feed[key]['description']
            data['pubDate'] = get_all_feed[key]['pubDate']
            data['updateDate'] = get_all_feed[key]['updateDate']
            
            serializer = ValidateInfo(data = data)
            if serializer.is_valid():
                database_entry = serializer.save(data)
                data["success_response"] = "Successfully refgistered an entry"
            else:
                data = serializer.errors
    return Response(data)

                
        

        
    # data['guid'] = get_all_feed
    # print(get_all_feed)

    # return get_all_feed
    # if request.method == 'POST':
    #     serializer = ValidateInfo(data = request.data)





##Create

##Retrieve

##Update

##Delete

##PUT

##PATCH