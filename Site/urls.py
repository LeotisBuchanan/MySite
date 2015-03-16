from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', include('home.urls', namespace='home')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^home/', include('home.urls', namespace='home')),

    url(r'^admin/', include(admin.site.urls)),
)
