from django.conf.urls import url
from django.contrib import admin

from schools import urls as school_urls

urlpatterns = [
    url(r'schools/', school_urls,),
    url(r'^admin/', admin.site.urls),
]
