from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField, RichTextField

from blog.blocks import BlogStreamBlock


@register_snippet
class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    content = StreamField(BlogStreamBlock(), blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('content'),
    ]

    def __str__(self):
        return self.title
