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

Contribution are welcome as always. Checkout the existing issues or create issues.

Steps for contributing:

- Fork and clone the repository

- If resolving an issue then create a branch with name like `bugfix-#<issue_number>` or `enhancement-#<issue_number>`

- After commiting, push the branch to your upstream fork.

<<<<<<< HEAD
- Create a Pull request to this repository


# CodeShare API
##GET
###By id
domain/api/*id*.json
###by filename
domain/api/*filename*.json


##POST
see json format at [CodeShare](http://domain/api.com)
###new code file
domain/api
###update existing file
domain/api/*filename or id*

####Every Post request will give the new object made or updated ,in response
=======
- Create a Pull request to this repository
>>>>>>> 5404f72... updated README.md with installation instructions and contributing guide
