from django.utils.translation import ugettext as _

from wagtail.core.blocks import (
    CharBlock, RichTextBlock, TextBlock,
    StreamBlock, StructBlock, ChoiceBlock
)

from wagtailcodeblock.blocks import CodeBlock

from base.choices import LINK_TARGET_CHOICES


class SubHeadingBlock(StructBlock):
    sub_heading = TextBlock(required=True)

    class Meta:
        icon = 'title'
        template = 'base/blocks/sub_heading_block.html'
        label = 'Sub Heading'


class ContentBlock(StructBlock):
    content = RichTextBlock()

    class Meta:
        icon = 'pilcrow'
        template = 'base/blocks/content_block.html'
        label = 'Content'


class CtaBlock(StructBlock):
    link = CharBlock()
    link_text = CharBlock()
    target = ChoiceBlock(LINK_TARGET_CHOICES, blank=True, required=False, help_text=_('Default is Same Window'))

    class Meta:
        icon = 'link'
        template = 'base/blocks/cta_block.html'
        label = 'CTA'


class CodeBlockBlock(StructBlock):
    code = CodeBlock(label='Code')


class HTMLBlock(StructBlock):
    html = TextBlock(classname='code', required=True)

    class Meta:
        icon = 'code'
        template = 'base/blocks/html_block.html'
        label = 'HTML'


# STREAM BLOCKS
class BaseStreamBlock(StreamBlock):
    """
    Combo block of all StructBlocks
    """
    sub_heading_block = SubHeadingBlock()
    content_block = ContentBlock()
    cta_block = CtaBlock()
    code_block = CodeBlockBlock()
    html_block = HTMLBlock()

    required = False
