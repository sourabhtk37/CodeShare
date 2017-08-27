from django.template import loader
from django.http import (
    HttpResponseNotFound,
    HttpResponseServerError,
    HttpResponseForbidden,
    HttpResponseBadRequest,
)


def page_not_found_view(request):
    t = loader.get_template('error/HTTP404.html')
    html = html = t.render({})
    return HttpResponseNotFound(html)


def my_custom_error_view(request):
    t = loader.get_template('error/HTTP500.html')
    html = html = t.render({})
    return HttpResponseServerError(html)


def permission_denied_view(request):
    t = loader.get_template('error/HTTP403.html')
    html = html = t.render({})
    return HttpResponseForbidden(html)


def bad_request_view(request):
    t = loader.get_template('error/HTTP400.html')
    html = html = t.render({})
    return HttpResponseBadRequest(html)
