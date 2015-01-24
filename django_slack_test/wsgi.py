
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_slack_test.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
