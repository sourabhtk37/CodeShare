from rest_framework import serializers
from code_share.app_code_share.models import CodeShare


class Codeserializer(serializers.ModelSerializer):

    class Meta:
        model = CodeShare
        fields = "__all__"
