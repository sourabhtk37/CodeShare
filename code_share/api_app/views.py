from django.shortcuts import get_object_or_404 as goo404, redirect
from rest_framework.decorators import api_view
from .serializers import Codeserializer
from app_code_share.models import CodeShare
from rest_framework.response import Response
import random


@api_view(['GET', 'POST'])
def api_home(request):
    if request.method == 'GET':
        return Response({
            "id": 25, "code": "print 'hello world'",
            "hash_value": "1950850", "file_name": "file1"
        })
    if request.method == 'POST':
        serializer = Codeserializer(data=request.data)
        if serializer.is_valid():
            a = random.randrange(1, 6)
            hash_value = str(hash(serializer.validated_data["code"]))[a:a + 8]
            if "file_name" in serializer.validated_data.keys():
                file = serializer.validated_data["file_name"]
                check_file = CodeShare.objects.filter(file_name=file).exists()
                if check_file is True and file != '':
                    return Response({
                        "error": """Awww!! An error . Probably we might have a file with same name.
                         Damn those folks."""
                    })
            else:
                file = None
            try:
                CodeShare.objects.create(
                    code=serializer.validated_data["code"],
                    hash_value=hash_value,
                    file_name=file
                )
                return redirect('return_by_hash', hash_id=hash_value)
            except Exception:
                return Response({"error": 'same hash error '})
        else:
            return Response("error occured")


@api_view(['GET', 'POST'])
def code_by_hash(request, hash_id, format=None):
    if request.method == 'GET':
        code_share = goo404(CodeShare, hash_value=hash_id)
        serialized_code = Codeserializer(code_share)
        return Response(serialized_code.data)
    if request.method == 'POST':
        code_obj = goo404(CodeShare, hash_value=hash_id)
        serializer = Codeserializer(code_obj, data=request.data)
        if serializer.is_valid():
            serializer.validated_data["file_name"] = code_obj.file_name
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("error occured")


@api_view(['GET', 'POST'])
def code_by_filename(request, file_name, format=None):
    if request.method == 'GET':
        code_share = goo404(CodeShare, file_name=file_name)
        serialized_code = Codeserializer(code_share)
        return Response(serialized_code.data)
    if request.method == 'POST':
        code_obj = goo404(CodeShare, file_name=file_name)
        serializer = Codeserializer(code_obj, data=request.data)
        if serializer.is_valid():
            serializer.validated_data["file_name"] = code_obj.file_name
            serializer.save()
            return Response(serializer.data)
        return Response("error occured")
