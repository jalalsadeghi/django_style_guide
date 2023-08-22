from .base import *  # noqa

CELERY_BROKER_BACKEND = "memory"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

from config.settings.debug_toolbar.settings import *  # noqa
