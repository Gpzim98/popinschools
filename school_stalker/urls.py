from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^', include('apps.core.urls', namespace=u"core")),
    url(r'^schools/', include('apps.schools.urls', namespace=u"schools")),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^admin/', admin.site.urls),
]
