SPECTACULAR_SETTINGS = {
    'TITLE': '{{cookiecutter.project_name}} API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

{%- if cookiecutter.use_auth == "dj-rest-auth" %}
REST_AUTH = {
    'SESSION_LOGIN': True,
    'OLD_PASSWORD_FIELD_ENABLED': True,
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'auth',
    'JWT_AUTH_HTTPONLY': False,
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = False
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'optional'


SWAGGER_SETTINGS = {
    'LOGIN_URL': 'login/',
    'LOGOUT_URL': 'logout/',
}
{%- endif %}


