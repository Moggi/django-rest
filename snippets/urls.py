from django.urls import re_path
from snippets import views

urlpatterns = [
    re_path(r'^$', views.SnippetList.as_view()),
    re_path(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]
