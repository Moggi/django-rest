from django.urls import re_path
from snippets import views

urlpatterns = [
    re_path(r'^$', views.SnippetList.as_view(), name='snippet-list'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    re_path(r'^(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]
