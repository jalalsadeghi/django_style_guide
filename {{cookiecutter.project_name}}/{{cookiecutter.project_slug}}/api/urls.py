from django.urls import path, include

urlpatterns = [
{%- if cookiecutter.files == "y" %}
    path('files/', include(('{{cookiecutter.project_slug}}.files.urls', 'files'))),
{%- endif %}
]
