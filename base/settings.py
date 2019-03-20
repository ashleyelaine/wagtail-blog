from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, FieldPanel


@register_setting
class GlobalSettings(BaseSetting):
    logo = models.FileField(upload_to='images/', null=True, blank=True)
    logo_text = models.CharField(max_length=255, null=True, blank=True, help_text='Add logo as text or use for logo alt text.')

    first_tab_panels = [
        FieldPanel('logo'),
        FieldPanel('logo_text'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(first_tab_panels, heading='Header'),
    ])

    class Meta:
        verbose_name = 'Global Settings'
