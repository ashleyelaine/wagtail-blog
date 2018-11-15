from django.contrib import sitemaps


class DefaultSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return ['/']


DEFAULT_SITEMAPS = {
    'pages': DefaultSitemap,
}
