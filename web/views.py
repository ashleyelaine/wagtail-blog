from django.shortcuts import render


def do404(request):
    return render(request, '404.html', request)


def do500(request):
    return render(request, '500.html', request)
