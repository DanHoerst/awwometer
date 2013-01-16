from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import Aww.views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Aww.views.default_display, name="default"),
    url(r'^vote/(?P<animal_up>[\w|\W]+)/(?P<animal_down>[\w|\W]+)/$', Aww.views.vote, name="vote"),
)
