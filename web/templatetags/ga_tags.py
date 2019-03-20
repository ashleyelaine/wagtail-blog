from django.conf import settings
from django.utils.html import format_html

from django import template
register = template.Library()


def _tracking_script(setting_name, script):
    tag_id = getattr(settings, setting_name, None)

    if not tag_id:
        return ''

    return format_html(script, tag_id)


@register.simple_tag
def google_analytics():
    return _tracking_script('GOOGLE_ANALYTICS_ID', """
        <!-- Global Site Tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={0}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments)}};
            gtag('js', new Date());
            gtag('config', '{0}');
        </script>
    """)
