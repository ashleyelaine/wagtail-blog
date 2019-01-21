from django.shortcuts import render
from django.views.generic.list import ListView

from blog.snippets import Post


class PostListView(ListView):

    model = Post
    paginate_by = 10  # if pagination is desired
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def do404(request):
    return render(request, '404.html', request)


def do500(request):
    return render(request, '500.html', request)
