import csv, requests
import urllib.request
from bs4 import BeautifulSoup
from dateutil import parser
from dateutil import tz
import dateutil




#https://stackoverflow.com/jobs/feed
# * title
# * GUID
# * Company
# * Categories (multiple)
# * description
# * Timestamps

class WebScrapper:
    """
        Takes url as input return a dictionary with appropriate key and values
        Parameters:

            urls (string) = A url as string

        Returns:
                A dictionary 

        """

    def __init__(self, url, *args):

        self.url = url
        self.info = {}
        
    def get_data(self):
        # url = "https://stackoverflow.com/jobs/feed"
        response = requests.get(self.url)
        soup= BeautifulSoup(response.content,"lxml-xml")
        items = soup.find_all('item')
        
        for item in items:
            guid = list(item.find_all('guid'))[0].get_text()                                            #GUID
            
            title = list(item.find_all('title'))[0].get_text()                                          #Title
            
            company_name = list(item.find_all('name'))[0].get_text()                                    #Company
            
            timezone_info = {"UT": dateutil.tz.UTC}

            pubDate = parser.parse(list(item.find_all('pubDate'))[0].get_text(), tzinfos=timezone_info)
                                                                                                        #Timestamp
            updated = parser.parse(list(item.find_all('updated'))[0].get_text(), tzinfos=timezone_info)
                
            categories = []
            for category in item.find_all('category'):
                categories.append(category.get_text())                                                  #Categories
            

            for description in item.find_all('description'):
                description = description.get_text()                                                    #Description
            
            self.info.update({guid: {"title":title, 
                                        "company":company_name, 
                                        "categories":categories,
                                        "description":description, 
                                        "pubDate":pubDate,
                                        "updated":updated}})
        
        return self.info
