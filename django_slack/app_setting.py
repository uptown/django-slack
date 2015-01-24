
SLACK_CLIENT_ID = None
SLACK_CLIENT_SECRET = None
SLACK_REDIRECT_URI = None
SLACK_DEFAULT_SCOPE = None
SLACK_DEFAULT_TEAM = None

try:
    from django.conf import settings
    SLACK_CLIENT_ID = getattr(settings, 'SLACK_CLIENT_ID', None)
    SLACK_CLIENT_SECRET = getattr(settings, 'SLACK_CLIENT_SECRET', None)
    SLACK_REDIRECT_URI = getattr(settings, 'SLACK_REDIRECT_URI', None)
    SLACK_DEFAULT_SCOPE = getattr(settings, 'SLACK_DEFAULT_SCOPE', None)
    SLACK_DEFAULT_TEAM = getattr(settings, 'SLACK_DEFAULT_TEAM', None)
except AttributeError:
    pass
except ImportError:
    pass


def set_slack_setting(client_id=None, client_secret=None, redirect_uri=None, default_scope=None, default_team=None):
    global SLACK_CLIENT_SECRET, SLACK_DEFAULT_SCOPE, SLACK_REDIRECT_URI, SLACK_CLIENT_ID, SLACK_DEFAULT_TEAM
    SLACK_CLIENT_ID = client_id
    SLACK_CLIENT_SECRET = client_secret
    SLACK_REDIRECT_URI = redirect_uri
    SLACK_DEFAULT_SCOPE = default_scope
    SLACK_DEFAULT_TEAM = default_team