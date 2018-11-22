from django.utils.translation import ugettext as _

from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import (
    CharBlock, RichTextBlock, TextBlock,
    StreamBlock, StructBlock, ChoiceBlock
)
from wagtail.core import blocks

from blog.choices import LINK_TARGET_CHOICES


class ContentBlock(StructBlock):
    content = RichTextBlock()

    class Meta:
        icon = 'pilcrow'
        template = 'base/blocks/content_block.html'
        label = 'Content'


class SubHeadingBlock(StructBlock):
    sub_heading = TextBlock(required=True)

    class Meta:
        icon = 'title'
        template = 'base/blocks/sub_heading_block.html'
        label = 'Sub Heading'


class CtaBlock(StructBlock):
    link = CharBlock()
    link_text = CharBlock()
    target = ChoiceBlock(LINK_TARGET_CHOICES, blank=True, required=False, help_text=_('Default is Same Window'))

    class Meta:
        icon = 'link'
        template = 'base/blocks/cta_block.html'
        label = 'CTA'


# STREAM BLOCKS
class BlogStreamBlock(StreamBlock):
    """
    Combo block of all StructBlocks
    """
    content_block = ContentBlock()
    sub_heading_block = SubHeadingBlock()
    cta_block = CtaBlock()

    required = False