from django.conf.urls.defaults import *
from rss.feeds import iTunesPodcastsFeed
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
	(r'^podcast/rss/$', iTunesPodcastsFeed()),
	 url(r'^admin/', include(admin.site.urls)),
)
