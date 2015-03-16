from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
        url(r'^$', views.MainView.as_view(), name='blog_main'),
        url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='blog_detail'),
        url(r'^contact/$', views.contact, name='blog_contact'),
        #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
        #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
        #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
        )
