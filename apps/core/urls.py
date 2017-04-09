from django.conf.urls import url, include
from rest_framework import routers

from .views import HomeView

from ..schools.api.view import SchoolViewSet
router = routers.DefaultRouter()

router.register(r'schools', SchoolViewSet)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="homepage"),
    url(r'^api/', include(router.urls)),
]


