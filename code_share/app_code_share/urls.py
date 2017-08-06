from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', home, name='app_home'),
    url(r'^app/(?P<hash_id>\w+)/$', view_by_hash, name='view_by_hash'),
    # url(r'^app/(?P<file_name>[\w-]+)/$', view_by_file, name='view_by_file')
]
