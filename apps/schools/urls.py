from django.conf.urls import url

from .views import SchoolList

urlpatterns = [
    url(r'$', SchoolList.as_view(), name='school-list'),
]
