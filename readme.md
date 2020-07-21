# DaCodes-courses

# Technology Stack

   [Lucichart - Build ERD](https://www.lucidchart.com/)
   
   [Django framework 3.0.7](https://www.djangoproject.com/)

   [Django rest framework 3.11 - Build API Rest Ful](https://www.django-rest-framework.org/)

   [Google Storage](https://cloud.google.com/storage)

   [Firebase - Login and Register Users](https://firebase.google.com/?hl=es)
   
   [Postgres](https://www.postgresql.org/)

   [sqlite3](https://www.sqlite.org/)

# Install

Create virtual enviroment

    virtualenv -p python3 env

Clone the project and run the commands as show in the order inside the virtual enviroment.

### Note: Download .env - enviroment's variables and Keys with format .json

1. Install all the requirements

    `pip install -r requirements/requirements_develop.txt`

2. Make migrations

    `python manage.py makemigrations`

3. Migrate the migrations

    `python manage.py migrate`

4. Create super user

    `python manage.py createsuperuser`

5. Run server

    `python manage.py runserver`

# Test Endpoints

Generate CustomToken from firebase

`python firebase_generate_token.py`

Request post to next endpoint Firebase for get_IDToken
`https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken`

With queryparams:

    Key: FIREBASE_PROJECT_KEY
    token: CustomToken
    returnSecureToken: true

Response:

    idToken: 'eyJhbGciOiJSUzI1NiIsImtpZ...'


# Endpoints
   [Dacodes Courses API Documentation](https://documenter.getpostman.com/view/11766693/T1DmDyPy)

# Entity Relationship Diagram
![Image](https://storage.googleapis.com/bucket-dacodes-courses/Dacodes-Courses.png)