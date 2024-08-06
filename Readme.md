# it is a Django project With REST APIS
This project is a backend test case to practice Django Rest APIs. it is about a teamMembers CRUD operations on SQLite DB.
I had no prior knowledge of Django or Python, this project took an average of 12 hours from reading the documentation and starting the actual development.

## Installation

```bash
# you have to create a virtual ENV first
python3 -m venv .venv

# activate it 
source .venv/bin/activate

# django should be installed, install it by runing this command
pip install django

# install django Rest Framework
pip install djangorestframework

# Run the server
python manage.py runserver

```

## Note

```bash
# let django Create a project called teamManagement, known in this readme as Project_Name (this project is created in this Code repository)
django-admin startproject teamManagement

# create a super user to login to the Django admin page (monitor the DB)
python manage.py createsuperuser
# to see the app in the admin panel you have to create (It is created in this project) admin.py and restart the server

# To CREATE APIS
# you have to make sure that rest_framework,Project_Name and is added to settings.py into the INSTALLED_APPS

```

## Good to know

## Note
The followed documentation for this project is [here](https://docs.djangoproject.com/en/5.0/)

```
This project uses APIS for CRUD operations, model forms and generic class-based views. it is consumed by a REACT project that you can find in the link below
```
[React Project](https://github.com/chakourix/isw-test-case-react) link is here
