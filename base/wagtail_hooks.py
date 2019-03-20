import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import BlockElementHandler
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from wagtail.core import hooks

from taggit.models import Tag

from .snippets import BlogCategory
from .models import PostPage


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'snippets']


class BlogCategoryAdmin(ModelAdmin):
    model = BlogCategory
    menu_label = 'Categories'
    menu_icon = 'plus'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'slug')


class BlogTagAdmin(ModelAdmin):
    model = Tag
    menu_label = 'Tags'
    menu_icon = 'plus'
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'slug')


class PostPageAdmin(ModelAdmin):
    model = PostPage
    menu_label = 'Posts'
    menu_icon = 'edit'
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False


class BlogAdminGroup(ModelAdminGroup):
    menu_label = 'Blog'
    menu_icon = 'grip'
    menu_order = 200
    items = (PostPageAdmin, BlogCategoryAdmin, BlogTagAdmin)


modeladmin_register(BlogAdminGroup)


###########################################
# Extending the Draftail Editor
###########################################
@hooks.register('register_rich_text_features')
def register_blockquote_feature(features):
    """
    Registering the `blockquote` feature, which uses the `blockquote` Draft.js block type,
    and is stored as HTML with a `<blockquote>` tag.
    """
    feature_name = 'blockquote'
    type_ = 'blockquote'
    tag = 'blockquote'

    control = {
        'type': type_,
        'label': '❝',
        'description': 'Blockquote',
        # Optionally, we can tell Draftail what element to use when displaying those blocks in the editor.
        'element': 'blockquote',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {tag: BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: tag}},
    })

    features.default_features.append('blockquote')
