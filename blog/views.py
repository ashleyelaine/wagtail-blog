from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.snippets import Post


class PostListView(ListView):

    model = Post
    paginate_by = 10  # if pagination is desired
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    slug_url_kwarg = 'slug'

    # def get_queryset(self):
    #     queryset = Post.objects.order_by('-published_date', '-created_date')

    #     if not self.request.user.is_superuser:
    #         queryset = queryset.filter(published=True)

    #     return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context