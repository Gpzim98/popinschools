from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import routers

from schools import views

from .views import SchoolCreate, SchoolProfile, SchoolList

router = routers.DefaultRouter()
router.register(r'schools', views.SchoolSerializerViewSet)

urlpatterns = [
    url(r'create/', SchoolCreate.as_view(), name='school-create'),
    url(r'profile/(?P<pk>\d+)/$', SchoolProfile.as_view(), name='school-profile'),
    url(r'list/$', SchoolList.as_view(), name='school-list')
]

urlpatterns += staticfiles_urlpatterns()
