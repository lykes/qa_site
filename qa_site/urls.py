from django.conf.urls import patterns, include, url

from questions.views import QuestionListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', QuestionListView.as_view(), name='list'),
    url(r'^questions/', include('questions.urls', namespace='questions')),
    url(r'^admin/', include(admin.site.urls)),
)
