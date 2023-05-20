# Project setup steps
- clone the project
- download Docker and start docker UI
- open terminal and go to the root folder (as given below) of the project `book_management`
- run command `docker-compose up` in terminal and wait for the project to be built
- open URL http://localhost:8000/swagger to list all the APIs and test them

# Local Development Run
- run `docker-compose up --build` to start the application
- close app by running command `docker-compose down` or simply press `Ctrl+C`

# Folder Structure
- `book_management` the book management project
- `books` the book app contains the book model and views
- `docker-compose.yml` - mysql and django services defined here
- `Dockerfile` - for the django app
- `manage.py`
- `requirements.txt`


```
book_management/
├── book_management/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── books
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── readme.md
└── requirements.txt
```

created with ❤️ by [Bipin Bhartola](bipin94179@gmail.com)
