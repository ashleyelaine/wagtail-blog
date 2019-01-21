from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.core import hooks

from .snippets import Post


@hooks.register('construct_main_menu')
def hide_documents_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'documents']


class PostSnippetAdmin(ModelAdmin):
    model = Post
    menu_label = 'Posts'
    menu_icon = 'plus'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title',)
    search_fields = ('title',)


modeladmin_register(PostSnippetAdmin)