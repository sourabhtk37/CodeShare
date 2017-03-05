from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app_code_share.views import *

urlpatterns = [
    url(r'^admin', admin.site.urls),
	url(r'^', include('app_code_share.urls', namespace='code_share')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
