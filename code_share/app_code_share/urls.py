from django.conf.urls import url,include
from .views import home, view_by_hash,CodeCreateView
from rest_framework.urlpatterns import format_suffix_patterns as suffix

from .serializers import Codeserializer
from .models import CodeShare
from rest_framework import generics

#app urls goes here
app_urls=[
    url(r'^$', home, name='app_home'),
    url(r'^(?P<hash_id>\w+)/$', view_by_hash, name='view_by_hash'),
]

#api url goes here
api_urls=[
    url(r'^$', CodeCreateView.as_view()),
    url(r'^(?P<hash_value>\w+)/$', generics.RetrieveUpdateAPIView.as_view(serializer_class=Codeserializer,queryset=CodeShare.objects.all(),lookup_field='hash_value')),
]
api_urls = suffix(api_urls,allowed=['json'])

urlpatterns = [
    url(r'^app/', include(app_urls)),
    url(r'^api/',include(api_urls))
    

]
