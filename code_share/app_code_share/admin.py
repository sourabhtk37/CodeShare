from django.contrib import admin
from .models import CodeShare


@admin.register(CodeShare)
class CodeShareAdmin(admin.ModelAdmin):
     exclude = ('id',)
     list_display = ('hash_value', 'language','file_name')
