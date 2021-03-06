from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    url(
        r'(?P<slug>[\w-]+)/votes/$',
        views.DeputeVoteListView.as_view(),
        name='depute_depute_vote_list',
    ),
    url(
        r'tous-les-deputes/$',
        views.DeputeListView.as_view(),
        name='depute_depute_list',
    ),
    url(
        r'(?P<slug>[\w-]+)/$',
        views.DeputeDetailView.as_view(),
        name='depute_depute_detail',
    ),
)
