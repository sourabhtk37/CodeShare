from rest_framework import serializers
from app_code_share.models import CodeShare

class Codeserializer(serializers.ModelSerializer):
  """
  Used to convert and map model Codeshare with API 
  format(json)

  """
  hash_value=serializers.CharField(read_only=True)
  
  class Meta:
      model = CodeShare
      fields ="__all__"

