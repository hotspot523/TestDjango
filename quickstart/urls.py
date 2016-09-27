__author__ = 'khemraj'
from django.conf.urls import url
from quickstart import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #api for function based view
    #url(r'^snippets/$', views.snippet_list),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)