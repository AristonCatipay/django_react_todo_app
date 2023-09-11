# Task Manager Application Backend

Task Manager Application is a full stack application using Django and React JS.
The user can ADD, EDIT, DELETE their task.

## Run Locally

To use this application you can clone two repository using git bash.
 - BACKEND - django_react_todo_app (this repository)
 - FRONTEND - django_react_todo_app_frontend


### Clone the repository
- Open the directory you want this application to be cloned. 
- Open git bash.

```bash
git clone https://github.com/AristonCatipay/django_react_todo_app.git
```

### Install Dependencies

Activate virtual environment
```bash
pipenv shell
```

Install Django
```bash
pipenv install django
```

Install Django CORS Headers
```bash
pipenv install django-cors-headers
```

Install Django REST Framework
```bash
pipenv install djangorestframework
```

Install MySQL Client
```bash
pipenv install mysqlclient
```

Migrate
```bash
python manage.py migrate
```

Start the server
```bash
python manage.py runserver
```

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)