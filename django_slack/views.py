from django.views.generic import View
from django.shortcuts import HttpResponse, HttpResponseRedirect
from .client import default_client
from .utils import generate_random_from_vschar_set
from .exceptions import SlackUnknownError


_SLACK_OAUTH2_STATE_SESSION_KEY = "kSlackOAuth2StateSessionKey"


class SlackOAuth2ClientView(View):

    def get(self, request):
        if request.GET.get('code'):
            code = request.GET.get('code')
            state = request.GET.get('state')
            if hasattr(request, "sessions") and state and state != request.sessions[_SLACK_OAUTH2_STATE_SESSION_KEY]:
                raise SlackUnknownError()
            token = default_client.oauth2_step2_issue_token(code=code)
            print(token)
            return HttpResponse()
        else:
            state = generate_random_from_vschar_set()
            if hasattr(request, "sessions"):
                request.sessions[_SLACK_OAUTH2_STATE_SESSION_KEY] = state
            return HttpResponseRedirect(default_client.oauth2_step1_url(state=state))