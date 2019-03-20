from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter


class TaggitListFilter(SimpleListFilter):
    """
    A custom filter class that can be used to filter by taggit tags in the admin.
    """

    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('tags')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'tag'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each tuple is the coded value
        for the option that will appear in the URL query. The second element is the
        human-readable name for the option that will appear in the right sidebar.
        """
        listing = []
        tags = model_admin.model.tags.all().order_by('name')
        for tag in tags:
            listing.append((tag.name, _(tag.name)))
        return listing

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value provided in the query
        string and retrievable via `self.value()`.
        """
        if self.value() is not None:
            return queryset.filter(tags__name=self.value())
