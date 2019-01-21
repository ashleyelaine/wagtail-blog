from django.db import models
from django.template.defaultfilters import slugify, truncatewords


from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField, RichTextField

from blog.blocks import BlogStreamBlock

from blog.utils import get_unique_slug


@register_snippet
class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    slug = models.SlugField(blank=True, max_length=140, unique=True)
    content = StreamField(BlogStreamBlock(), blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        StreamFieldPanel('content'),
    ]

    def __str__(self):
        return self.title

    @property
    def short_title(self):
        return truncatewords(self.title, 5)

    def get_absolute_url(self):
        return "/%s/" % (self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'short_title', 'slug')
        super().save(*args, **kwargs)
