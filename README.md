# a cookiecutter based on django_styleguide

The basic idea of this structure is derived from [CookieCutter](https://github.com/cookiecutter/cookiecutter-django), developed by Team [HackSoftware](https://github.com/HackSoftware/Django-Styleguide), and I got acquainted with this project through [Amir Bahadur](https://github.com/amirbahador-hub/django_style_guide), and I am trying to develop it based on my personal experience and market needs.

- If you have problems with django_style_guide, please open [issues](https://github.com/jalalsadeghi/django_style_guide/issues/new) don't send
  emails to the maintainers.

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

## usage

install cookiecutter

```
pip install cookiecutter
```

setup the project

```
cookiecutter https://github.com/jalalsadeghi/django_style_guide.git
```
