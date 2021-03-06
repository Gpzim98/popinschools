from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('apps.core.urls', namespace=u"core")),
    url(r'^schools/', include('apps.schools.urls', namespace=u"schools")),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
