from django.conf.urls import include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^', include('web.urls')),
    url(r'^admin/', admin.site.urls),
]
