import json
from utils.scrawler import WebScrapper

class ManageBulkEntry:

    def __init__(self, jsonData=None, urls = None):

        """
        Takes either jsondata or urls as input or both 
            and return a dictionary with appropriate key and values
        Parameters:

            jsonData (list) = List of list contains nested dictionaries         eg. [[{}, {}, {}], [{}, {}, {}, {}]]     
            urls (list) = List of urls                                          eg. ["","","", ""]                               ## 

        Returns:
                A dictionary 

            
        """
        self.jsondata = jsonData
        self.urls = urls
        self.info = {} 
        
    def bulkentry(self):
        if self.jsonData:
            list_of_data = json.loads(self.jsondata)
            for each_list in list_of_data:
                for each_dictionary in each_list:
                    self.info.update(each_dictionary)
        if self.urls:
            list_of_urls = json.loads(self.urls)
            for url in list_of_urls:
                get_data = WebScrapper(url = url).get_data()
                for key, value in get_data.items():
                    value['guid'] = key
                    value['categories'] = ",".join(str(category) for category in value['categories'] )
                    self.info.update(value)
        return self.info
        
    


            




