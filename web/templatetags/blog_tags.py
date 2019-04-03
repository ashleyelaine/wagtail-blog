from django import template
from base.models import PostPage

register = template.Library()


@register.inclusion_tag('tags/tags.html', takes_context=True)
def tags(context):
    return {
        'tags': PostPage.tags.most_common()[:10],
        'request': context['request'],
    }
