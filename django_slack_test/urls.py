from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^oauth2/', include('django_slack.urls'))
)
