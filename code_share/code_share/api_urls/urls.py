from django.conf.urls import url
from app_code_share.views import CodeCreateView
from rest_framework.urlpatterns import format_suffix_patterns as suffix
from app_code_share.serializers import Codeserializer
from app_code_share.models import CodeShare
from rest_framework import generics

urlpatterns=[
    url(r'^$', CodeCreateView.as_view()),
    url(r'^(?P<hash_value>\w+)/$', generics.RetrieveUpdateAPIView.as_view(serializer_class=Codeserializer,queryset=CodeShare.objects.all(),lookup_field='hash_value')),
]
urlpatterns = suffix(urlpatterns,allowed=['json'])
