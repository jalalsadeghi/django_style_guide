# a cookiecutter based on django_styleguide

The basic idea of this structure is derived from [CookieCutter](https://github.com/cookiecutter/cookiecutter-django), which was developed by the [HackSoftware team in Django Styleguide](https://github.com/HackSoftware/Django-Styleguide), and I got acquainted with this project through [Amir Bahadur](https://github.com/amirbahador-hub/django_style_guide), and I am trying to develop it based on my personal experience and market needs.

- If you have problems with django_style_guide, please open [issues](https://github.com/jalalsadeghi/django_style_guide/issues/new).

## Features

- For Django 4.2
- Works with Python 3.11
- Renders Django projects with 100% starting test coverage 
- Optimized development and production settings
- Registration via [dj-rest-auth](https://github.com/iMerica/dj-rest-auth/tree/master/demo)
- Media storage using Amazon S3, Google Cloud Storage, Azure Storage or nginx
- Docker support using [docker-compose](https://github.com/docker/compose) for development and production
- Run tests with unittest or pytest
- Customizable PostgreSQL version

## Key features of [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide) include:

1. Coding standards: The styleguide defines coding standards and conventions to ensure consistent and readable code across Django projects.
2. Django project structure: The software outlines a recommended project structure for Django applications, including the organization of files and directories.
3. Django templates and views: The styleguide provides examples of Django templates and views, demonstrating how to create dynamic and interactive web pages.
4. Database models and migrations: The software covers the creation of database models using Django's Object-Relational Mapping (ORM) and the management of database migrations.
5. RESTful APIs: The styleguide includes examples of building RESTful APIs using Django's built-in capabilities, allowing for seamless integration with front-end interfaces.
6. Testing and debugging: The software emphasizes the importance of testing and debugging in Django development, providing guidelines for writing effective test cases and debugging techniques.

## usage

install cookiecutter

```
pip install cookiecutter
```

setup the project

```
cookiecutter https://github.com/jalalsadeghi/django_style_guide.git
```
