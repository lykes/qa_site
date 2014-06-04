from django.conf.urls import patterns, url

from .views import QuestionCreateView
from .views import QuestionDetailView
from .views import QuestionUpdateView

urlpatterns = patterns('',
    url(r'^create/$', QuestionCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', QuestionUpdateView.as_view(), name='update'),
)
