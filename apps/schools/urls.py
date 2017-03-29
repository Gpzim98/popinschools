from django.conf.urls import url

from .views import SchoolList, SchoolDetail

urlpatterns = [
    url(r'^$', SchoolList.as_view(), name='school-list'),
    url(r'profile/(?P<pk>\d+)/$', SchoolDetail.as_view(), name='school-profile'),
]
