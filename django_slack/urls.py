from django.conf.urls import patterns, url
from .views import SlackOAuth2ClientView

urlpatterns = patterns('',
    url(r'callback', SlackOAuth2ClientView.as_view())
)
