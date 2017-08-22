from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    page_not_found_view,
    my_custom_error_view,
    permission_denied_view,
    bad_request_view,
)

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^', include('app_code_share.urls', namespace='code_share')),
    url(r'^api/', include('api_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = page_not_found_view
handler500 = my_custom_error_view
handler403 = permission_denied_view
handler400 = bad_request_view
