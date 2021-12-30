## Introduction
It is a rest-api based web application written in Django which is able to automatically scrap data from any given url and store it into a database with pre-defined format.

### Features
- Loads an initial data from a web service and insert into database
- Able to perform certauin DB(Database) operations; such as create, retrieve, update, delete, put and patch
- It can scrwal to multiple web services or a big chunk of data to make entries in bulk to database

### User Instruction
To run this application a user will require the following approaches. I used python 3.6.9. 

Run requirements.txt with pip 
```
$ pip install -r requirements.txt
```
Manage your environment variables in the **.env** file. For instance change the database engine depending on which database you are using, change the database configuration if you want.

Run ``` $ python manage.py runserver ``` to execute the application.


### Endpoints
I have used swagger to maintain the api calls.
use ```http://localhost:8000/swagger/``` for more details. 

<hr> 


There is file named scrawler.py in utils folder which is responsible for crawling into a given url and parse the file to insert the unique entries to DB.
