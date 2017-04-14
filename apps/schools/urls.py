from django.conf.urls import url

from .views import SchoolList, SchoolDetail, SchoolComment, already_studied_here

urlpatterns = [
    url(r'^$', SchoolList.as_view(), name='school-list'),
    url(r'profile/(?P<pk>\d+)/$', SchoolDetail.as_view(), name='school-profile'),
    url(r'profile/(?P<pk>\d+)/alreadystdhere/$', already_studied_here,
        name='school-profile-alreadystdhere'),
    url(r'profile/(?P<pk>\d+)/comment/$', SchoolComment.as_view(),
        name='school-profile-comment'),
]
