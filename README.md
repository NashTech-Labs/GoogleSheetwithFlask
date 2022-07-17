# Template to To create a Flask API that perform CRUD operations on the google sheet

This template uses two Google Apis namely: Google Drive and Google Sheet and a Service account credentials to access the google sheet. The with help of the Python Script, we have a created an api that can add new sheets to present workbook of googlesheet, add information, update the information, view the information and even delete the information.

*************************************************************************************************************
## Requirements : 
*************************************************************************************************************
1. Account on GCP and Basic GCP Knowledge as well
2. Basic Knowledge of API and Python 

* NOTE: you can use local system or if wanted Deploy on https://www.pythonanywhere.com/

*************************************************************************************************************
## Steps : 
*************************************************************************************************************
### 1 : Enable API and Creating Service Account on GCP 

* Login to GCP and create a New Project or If wanted use the     default.
* Go to API Library into "Google Workspace" Section
* Enable "Google Sheet API" and "Google Drive API"
* Open Google Drive Api and Click Manage
* Left Side You get Credentials
* Click on "CREATE CREDENTIALS" button Select Service account
* follow this to create account --> 
https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-console
* create key for service account --> https://cloud.google.com/iam/docs/creating-managing-service-account-keys

* when key is downloaded name it credentials.json and move to app.py directory or provide the complete path in code as
'path_to_creds = "credentials.json"'

*************************************************************************************************************
### 2 : Add Service Account to Google Sheet

* Now you will see an email for service account is created, you can get it from Google Drive API --> Credentials
* Copy it and provide this email the edit rights in the google sheet you want to apply the CRUD operations
* Paste and gitve the permissions on sheet 
* copy the url and Paste it to code as 
'sheet_url = "https://docs.google.com/spreadsheets/d/12g-lce2EdDbJXGEUjcRW1saQYxHbTcCiscLp5pYImjE/edit?usp=sharing"'
 

*************************************************************************************************************
### 3 : Deploy the Application

#### LOCAL SYSTEM or cloud VM (Linux)

* Now you can run the app
```
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run --host=0.0.0.0 --port=9191

```
or 
```
$ python app.py

```
#### online deployment

* use sites like Heroku or Python Anywhere ('https://www.pythonanywhere.com/')

*************************************************************************************************************
### 4 : Using the API (Linux)

* The basic url uses "GET" method 
```
$ curl http://192.168.1.4:9191/

[
  [
    "title", 
    "Sheet1"
  ], 
  [
    "title", 
    "new"
  ]
]
```
* other method use "POST" method, so you nee to use header of json as in following example:
```
$ curl -H "Content-Type: application/json" -d '{"rows":20,"columns":100}' -X POST http://192.168.1.4:9191/create/sheet2/
[
  [
    "title", 
    "Sheet1"
  ], 
  [
    "title", 
    "new"
  ], 
  [
    "title", 
    "sheet2"
  ]
]

```

*************************************************************************************************************
### Recommendation: 
The whole code is directly made using python on flask framework. using this api you can access and create a database online that update easily. you can modify this code as per your requirement.

## Thank You!
*************************************************************************************************************