from django.urls import path, include

urlpatterns = [
{%- if cookiecutter.files == "y" %}
    path('files/', include(('djangostyleguide3.files.urls', 'files'))),
{%- endif %}
]
