from django.shortcuts import render,get_object_or_404 as goo404,redirect
from rest_framework.decorators import api_view
from .serializers import Codeserializer
from app_code_share.models import CodeShare
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from rest_framework import status


@api_view(['GET','POST'])
def api_home(request):
    if request.method == 'GET':
        return Response({"id": 25,"code":"print 'hello world'","hash_value": "1950850", "file_name": "file1"}) 
    if request.method == 'POST':
        code_share = request.POST.get('code_snippet')
        file_name = request.POST.get('file_name')
        hash_value = str(hash(code_share))[1:8]
        if CodeShare.objects.filter(file_name=file_name).exists() == True and file_name != '':
            return JsonResponse({"error":'Awww!! An error . Probably we might have a file with same name . Damn those folks.'},safe=False)
        CodeShare.objects.create(code=code_share, 
                                 hash_value=hash_value,
                                 file_name=file_name)  
        return redirect('return_by_hash', hash_id=hash_value)







@api_view(['GET','POST'])
def code_by_hash(request,hash_id,format=None):  
    if request.method == 'GET':
        code_share = goo404(CodeShare,hash_value=hash_id)
        serialized_code=Codeserializer(code_share)
        return Response(serialized_code.data)   
    if request.method == 'POST':
        code_share = request.POST.get('code_snippet')
        code_obj=goo404(CodeShare,hash_value=hash_id)
        serializer=Codeserializer(code_obj,data=request.data)
        if  serializer.is_valid():
                obj=serializer.save()
                obj.code=code_share
                obj.save()
                return Response(serializer.data)
        else:
            return JsonResponse("error occured")



@api_view(['GET','POST'])
def code_by_filename(request, file_name,format=None):   
    if request.method == 'GET':
        code_share = goo404(CodeShare,file_name=file_name)
        serialized_code=Codeserializer(code_share)
        return Response(serialized_code.data)        
    if request.method == 'POST':     
        code_share = request.POST.get('code_snippet')
        code_obj = goo404(CodeShare,file_name=file_name)
        serializer=Codeserializer(code_obj,data=request.data)
        if  serializer.is_valid():
                obj=serializer.save()
                obj.code=code_share
                obj.save()
                return Response(serializer.data)
        return JsonResponse("error occured")
# Create your views here.
