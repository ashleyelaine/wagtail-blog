from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query


def search(request):
    # Search
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = Page.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Render template
    return render(request, 'search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
    })


def do404(request, exception):
    return render(request, '404.html', request)


def do500(request):
    return render(request, '500.html', request)
