from django.conf.urls import url,include
from .views import home, view_by_hash

#app urls goes here
app_urls=[
    url(r'^$', home, name='app_home'),
    url(r'^(?P<hash_id>\w+)/$', view_by_hash, name='view_by_hash'),
]


urlpatterns = [
    url(r'^', include(app_urls)),
 
]
