from django.conf.urls import patterns, include, url
from django.contrib import admin

from home import views

urlpatterns = patterns('',
    # Examples:
    url(r'^grappelli/', include('grappelli.urls')),                    # Grappelli URLs
    url(r'^ckeditor/', include('ckeditor.urls')),

    #url(r'^$', include('home.urls', namespace='home')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^$', views.index, name='homepage'),

    url(r'^admin/', include(admin.site.urls)),                          # Admin URLs
)
