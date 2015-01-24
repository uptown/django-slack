import json
from .utils import generate_random_from_vschar_set, cached_property
from .with3 import urlencode, urlopen, HTTPError
from .exceptions import SlackSettingIsMissing, SlackUnknownError, SlackBadResponse
from .app_setting import SLACK_CLIENT_ID, SLACK_CLIENT_SECRET, SLACK_REDIRECT_URI, SLACK_DEFAULT_SCOPE, \
    SLACK_DEFAULT_TEAM


SLACK_AUTHORIZE_URL = "https://slack.com/oauth/authorize"
SLACK_TOKEN_ISSUE_URL = "https://slack.com/api/oauth.access"


class SlackClient(object):

    def __init__(self, client_id=None, client_secret=None, default_scope=None):
        self._client_id = client_id
        self._client_secret = client_secret

    def oauth2_step1_url(self, redirect_uri=SLACK_REDIRECT_URI, scope=SLACK_DEFAULT_SCOPE, state=None,
                         team=SLACK_DEFAULT_TEAM):
        client_id = self.client_id
        if not state:
            state = generate_random_from_vschar_set(length=10)
        query_pairs =  [('client_id', client_id), ('state', state)]
        if redirect_uri:
            query_pairs.append(('redirect_uri', redirect_uri))
        if scope:
            query_pairs.append(('scope', scope))
        if team:
            query_pairs.append(('team', team))
        return SLACK_AUTHORIZE_URL + "?" + urlencode(query_pairs)

    def oauth2_step2_issue_token(self, code, redirect_uri=SLACK_REDIRECT_URI):
        data={
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code
        }
        if redirect_uri:
            data['redirect_uri'] = redirect_uri
        data = urlencode(data).encode('utf8')
        try:
            ret = json.loads(urlopen(SLACK_TOKEN_ISSUE_URL, data=data).read().decode('utf8'))
        except HTTPError:
            raise SlackUnknownError()

        if ret['ok'] != 'false':
            raise SlackBadResponse(reason=ret['error'])
        return ret['access_token']

    @cached_property
    def client_id(self):
        if not self._client_id:
            raise SlackSettingIsMissing(field_name="client_id")
        return self._client_id

    @cached_property
    def client_secret(self):
        if not self._client_secret:
            raise SlackSettingIsMissing(field_name="client_secret")
        return self._client_secret


default_client = SlackClient(client_id=SLACK_CLIENT_ID, client_secret=SLACK_CLIENT_SECRET)