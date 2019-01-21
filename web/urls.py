from django.conf.urls import url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . import views
from web.views import PostListView

from wagtail.contrib.sitemaps.views import sitemap


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    url('^sitemap.xml$', sitemap),
]

handler404 = views.do404
handler500 = views.do500