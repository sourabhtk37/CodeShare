# CodeShare
A django application for sharing code snippets.


### Installation

- Create a virtual environment

    `virtualenv venv`


- Start virtual environment

    `source venv/bin/activate`


- Install requirements

    `pip install -r requirements`


- Enable Debug for debugging

    Go to the `settings.py` file and set the variable `DEBUG` to True.


- Migrate DB

    `python manage.py makemigrations` and `python manage.py migrate` 


- Running test server, go to the folder with `manage.py` file and run:

    `python manage.py runserver`

    This will run the server at localhost.


### Contributing
Please Checkout [CONTRIBUTING.md
](https://github.com/sourabhtk37/CodeShare/blob/master/CONTRIBUTING.md)
 



# CodeShare API

## GET

api.domain/*hashid*.json

### Data Format
```javascript  
id : 5
hash_value : "81b9uc7llmjm"
code : "print ('hello world')"
file_name "mypythoncode"
language : "python"

```



## POST

api.domain/

### Data Format
```javascript  

code : "print ('hello world')"
file_name "mypythoncode"
language : "python"

```

## PUT
api.domain/*hashid*/


### Data Format
```javascript  

code : "print ('hello world')"
file_name "mypythoncode"
language : "python"

```

####Every Post request will give the new object made or updated ,in response

#### Bug Fix

> The django-subdomains contains a small bug and here is the fix
 
 In your site-pakages/subdomains/middleware.py make a slightly change in you SubdomainMiddleware class

 ```python
 
from django.utils.deprecation import MiddlewareMixin

class SubdomainMiddleware(MiddlewareMixin):

```
