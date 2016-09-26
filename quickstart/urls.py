__author__ = 'khemraj'
from django.conf.urls import url
from quickstart import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    ]
