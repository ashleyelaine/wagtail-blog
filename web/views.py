from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def do404(request):
    return render(request, '404.html', request)


def do500(request):
    return render(request, '500.html', request)
