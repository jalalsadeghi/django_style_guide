from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static

from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView
from dj_rest_auth.registration.views import VerifyEmailView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='API Docs',
        default_version='v1',
    )
)

urlpatterns = [
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema'),
    path('admin/', admin.site.urls),
    path('api/', include(('{{cookiecutter.project_slug}}.api.urls', 'api'))),

    {%- if cookiecutter.use_auth == "dj-rest-auth" %}
    re_path(r'^', include('dj_rest_auth.urls')),

    re_path(r'^registration/$', include('dj_rest_auth.registration.urls')),
    re_path(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$',
            VerifyEmailView.as_view(),
            name='account_confirm_email',
            ),

    path(
        'api/password/reset/confirm/<str:uidb64>/<str:token>',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    {%- endif %}
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
