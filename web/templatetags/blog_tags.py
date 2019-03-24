from django import template
from base.snippets import BlogCategory

register = template.Library()


# Category snippets
@register.inclusion_tag('tags/categories.html', takes_context=True)
def categories(context):
    return {
        'categories': BlogCategory.objects.all(),
        'request': context['request'],
    }