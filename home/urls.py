from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
        #url(r'^$', views.index, name='homepage'),
        url(r'^resume/$', views.resume, name='resume'),
        url(r'^projects/$', views.projects, name='projects'),
        url(r'^contact/$', views.contact, name='contact'),
        )
