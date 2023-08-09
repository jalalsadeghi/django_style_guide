from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path('admin/', admin.site.urls),
    path('api/', include(('{{cookiecutter.project_slug}}.api.urls', 'api'))),
    {%- if cookiecutter.use_auth == 1 %}
    re_path(r'^', include('dj_rest_auth.urls')),

    re_path(r'^registration/$', include('dj_rest_auth.registration.urls')),
    re_path(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$',
            VerifyEmailView.as_view(),
            name='account_confirm_email',
            ),
    {%- endif %}
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
