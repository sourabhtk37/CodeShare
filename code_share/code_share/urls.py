from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^', include('app_code_share.urls', namespace='code_share')),
    url(r'^api/', include('api_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
