from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CodeShare
import hashlib


def home(request):

    if request.method == 'GET':
        return render(request, 'app_code_share/homepage.html',{})
    
    if request.method == 'POST':
        code_share = request.POST.get('code_snippet')
        file_name = request.POST.get('file_name')
        hash_value = str(hash(code_share))[1:8]
        try:
            CodeShare.objects.create(code=code_share, 
                                     hash_value=hash_value,
                                     file_name=file_name)
        except:
            return render('Awww!! An error. Probably you cannot have a same file name. Damn those folks.')

        return redirect('code_share:view_by_hash', hash_id=hash_value)


def view_by_hash(request, hash_id):
    
    if request.method == 'GET':
        code_share = CodeShare.objects.get(hash_value=hash_id)

        return render(request, 'app_code_share/homepage.html', {'code_share': code_share})
    
    if request.method == 'POST':
        code_share = request.POST.get('code_snippet')
        file_name = request.POST.get('file_name')
        code_obj = CodeShare.objects.get(hash_value=hash_id)
        code_obj.code = code_share
        code_obj.file_name = file_name
        code_obj.save()

        return redirect('code_share:view_by_hash', hash_id=hash_id)


def view_by_file(request, file_name):
    
    if request.method == 'GET':
        code_share = CodeShare.objects.get(file_name=file_name)

        return render(request, 'app_code_share/homepage.html', {'code_share': code_share})
    
    if request.method == 'POST':
        code_share = request.POST.get('code_snippet')
        file_name = request.POST.get('file_name')
        code_obj = CodeShare.objects.get(file_name=file_name)
        code_obj.code = code_share
        code_obj.file_name = file_name
        code_obj.save()

        return redirect('code_share:view_by_file', file_name=file_name)
