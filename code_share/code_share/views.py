from django.shortcuts import render


def page_not_found_view(request):
    return render(request, 'error/HTTP404.html', {})


def my_custom_error_view(request):
    return render(request, 'error/HTTP500.html', {})


def permission_denied_view(request):
    return render(request, 'error/HTTP403.html', {})


def bad_request_view(request):
    return render(request, 'error/HTTP400.html', {})
