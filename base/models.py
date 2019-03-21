from django import forms
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase
import datetime

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import (
    StreamFieldPanel, FieldPanel, FieldRowPanel,
    MultiFieldPanel, InlinePanel
)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index

from base.settings import GlobalSettings
from base.blocks import BaseStreamBlock, FAQBlock
from base.snippets import BlogCategory

__all__ = ['GlobalSettings']


class HomePage(Page):
    template = 'base/home_page.html'
    page_title_override = models.CharField(max_length=255, blank=True, help_text='Use if you would like the page title to be different than what appears in the navigation.')
    page_content = StreamField(BaseStreamBlock(), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_title_override'),
        StreamFieldPanel('page_content'),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = PostPage.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 2)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts
        return context



class BasePage(Page):
    template = 'base/base_page.html'
    page_title_override = models.CharField(max_length=255, blank=True, help_text='Use if you would like the page title to be different than what appears in the navigation.')
    page_content = StreamField(BaseStreamBlock(), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_title_override'),
        StreamFieldPanel('page_content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('page_title_override'),
        index.SearchField('page_content'),
    ]


class FaqPage(Page):
    template = 'base/faq_page.html'
    page_title_override = models.CharField(max_length=255, blank=True, help_text='Use if you would like the page title to be different than what appears in the navigation.')
    intro = models.TextField(blank=True)
    faqs = StreamField(
        [('FAQ', FAQBlock())],
        blank=True
    )
    page_content = StreamField(BaseStreamBlock(), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_title_override'),
        FieldPanel('intro'),
        StreamFieldPanel('faqs'),
        StreamFieldPanel('page_content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('page_title_override'),
        index.SearchField('intro'),
        index.SearchField('faqs'),
    ]

    class Meta:
        verbose_name = 'FAQ Page'


class BlogPage(RoutablePageMixin, Page):
    template = 'base/blog_page.html'
    subpage_types = ['PostPage']

    page_title_override = models.CharField(max_length=255, blank=True, help_text='Use if you would like the page title to be different than what appears in the navigation.')
    intro = models.TextField(blank=True)
    page_content = StreamField(BaseStreamBlock(), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_title_override'),
        FieldPanel('intro'),
        StreamFieldPanel('page_content'),
    ]

    def get_posts(self):
        return PostPage.objects.descendant_of(self).live()

    def get_context(self, request, *args, **kwargs):
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        context['posts'] = self.posts
        context['blog_page'] = self
        return context

    @route(r'^tag/(?P<tag>[-\w]+)/$')
    def post_by_tag(self, request, tag, *args, **kwargs):
        self.search_type = 'tag'
        self.search_term = tag
        self.posts = self.get_posts().filter(tags__slug=tag)
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^category/(?P<category>[-\w]+)/$')
    def post_by_category(self, request, category, *args, **kwargs):
        self.search_type = 'category'
        self.search_term = category
        self.posts = self.get_posts().filter(categories__slug=category)
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^$')
    def post_list(self, request, *args, **kwargs):
        self.posts = self.get_posts()
        return Page.serve(self, request, *args, **kwargs)


class PostPageTag(TaggedItemBase):
    content_object = ParentalKey('PostPage', on_delete=models.CASCADE, related_name='post_tags')


class PostPage(Page):
    template = 'base/post_page.html'
    parent_page_types = ['BlogPage']
    subpage_types = []

    intro = models.TextField(blank=True)
    date = models.DateTimeField(verbose_name='Post date', default=datetime.datetime.today)
    categories = ParentalManyToManyField(BlogCategory, blank=True)
    tags = ClusterTaggableManager(through=PostPageTag, blank=True)
    page_content = StreamField(BaseStreamBlock(), blank=True)
    seo_keywords = models.CharField(max_length=255, blank=True, help_text='Optional. Separate each keyword with a comma.')
    socials = models.BooleanField(verbose_name='Social Icons?', default=True)
    addthis_pubid = models.CharField(verbose_name='AddThis PubId', max_length=25, null=True, blank=True, help_text='This is the string that is AFTER `#pubid=`. Ex: ra-5a61fe428f3a39a8', default='5c8fad3d8f2fec06')

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
        StreamFieldPanel('page_content'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('seo_keywords'),
        FieldPanel('socials'),
        FieldPanel('addthis_pubid'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('date'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('categories'),
        index.SearchField('tags'),
        index.SearchField('page_content'),
    ]

    @property
    def blog_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(PostPage, self).get_context(request, *args, **kwargs)
        context['blog_page'] = self.blog_page
        context['post'] = self
        return context


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(WagtailCaptchaEmailForm):
    template = 'base/form_page.html'
    page_title_override = models.CharField(max_length=255, blank=True, help_text='Use if you would like the page title to be different than what appears in the navigation.')
    intro = models.TextField(blank=True)
    intro_content = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    page_content = StreamField(BaseStreamBlock(), blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('page_title_override'),
        FieldPanel('intro', classname='full'),
        FieldPanel('intro_content', classname='full'),
        InlinePanel('form_fields', label='Form fields'),
        FieldPanel('thank_you_text', classname='full'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], 'Email'),
        StreamFieldPanel('page_content'),
    ]
