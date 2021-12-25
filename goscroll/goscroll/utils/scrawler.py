import csv, requests
import xml.etree.ElementTree as ET
import urllib.request
from bs4 import BeautifulSoup

#https://stackoverflow.com/jobs/feed
# * title
# * GUID
# * Company
# * Categories (multiple)
# * description
# * Timestamps

class WebScrapper:

    def __init__(self, url, *args):

        self.url = url
        self.info = {}
        
    def get_data(self):

        # url = "https://stackoverflow.com/jobs/feed"
        url = self.url
        response = requests.get(self.url)
        soup= BeautifulSoup(response.content,"lxml-xml")
        itmes = soup.find_all('item')
        

        for item in itmes:
            for id in item.find_all('guid'):
                guid = id.get_text()                                            #GUID
            for title in item.find_all('title'):
                title = title.get_text()                                        #Title
            for name in item.find_all('name'):
                company_name = name.get_text()                                  #Company
            for pub_time in item.find_all('pubDate'):
                pubDate = pub_time.get_text()
            for updated_time in item.find_all('updated'):
                updated = updated_time.get_text()
                
            time_stamp = {"pubDate":pubDate, "updateDate":updated}                                #TimeStamps

            categories = []
            for category in item.find_all('category'):
                categories.append(category.get_text())                            #Categories
            
            for description in soup.find_all('description'):
                description = description.get_text()
            self.info.update({guid: {"title":title, 
                                        "company":company_name, 
                                        "category":categories,
                                        "description":description, 
                                        "pubDate":pubDate,
                                        "updateDate":updated}})
        
        return self.info
            # print("Self-info", self.info)
# print(info)




# print("Title = {} , GUID = {} , Companies = {} , Description = {}".format(len(titles), len(guids), len(companies), len(descriptions)))
# for description in soup.find_all('description'):
#     #print(list(description.children))
#     #print(description.get_text())
#     [print(type(item)) for item in list(description.children)]

# for title, description in soup.find_all('title'), soup.find_all('description'):
#     print("{} || {}".format(title.get_text(), description.get_text()))
    # print("list-format {} == unknown-format {}".format((list(title)),title))
    #print(soup.find_all('description'))