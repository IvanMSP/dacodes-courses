# DaCodes-courses

# Used Frameworks and technologies

    Django framework for build backend 

    Django rest framework for build api

    Google Storage to store images

    Postgres - DB for production and development

    sqlite3 - DB for testing

# Install

Create virtual enviroment

    virtualenv -p python3 env

Clone the project and run the commands as show in the order inside the virtual enviroment.

1. Install all the requirements

    `pip install -r requirements_develop.txt`

2. Make migrations

    `python manage.py makemigrations`

3. Migrate the migrations

    `python manage.py migrate`

4. Create super user

    `python manage.py createsuperuser`

5. Run server

    `python manage.py runserver`


# Endpoints
    api/auth/  - Auth endpoint
    api/courses/ - Get all courses available
    api/courses/<str:slug>/ - Get course detail
    api/courses/<str:slug>/lessons/ - Get all lessons of a course
    api/courses/<username>/ - Get all courses of a student
    api/lessons/<str:slug>/questions - Get all questions by course of a student


# Entity Relationship Diagram
![Image](https://storage.googleapis.com/bucket-dacodes-courses/Dacodes-Courses.png)