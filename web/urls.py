from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . import views

from django.contrib.sitemaps.views import sitemap
from .sitemap import DEFAULT_SITEMAPS


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': DEFAULT_SITEMAPS}),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.do404
handler500 = views.do500
