from django.shortcuts import render, redirect, get_object_or_404 as goo404
from .models import CodeShare
from django.contrib import messages
from django.utils.crypto import get_random_string


def home(request):
    """
    Homepage and creation of code snippet

    GET:
        returns the homepage

        :return renders the homepage.html

    POST:
        handles the request for creating a code snippet

        :param code_snippet: code content from the text box
        :param file_name: if file name is specified, it is not None

        :return redirect to view_by_hash method with unique ID has param

    """

    if request.method == 'GET':
        return render(request, 'app_code_share/homepage.html', {})

    if request.method == 'POST':
        code_share = request.POST.get('code_snippet')
        file_name = request.POST.get('file_name')
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        hash_value = get_random_string(8, chars)
        file_exist = CodeShare.objects.filter(file_name=file_name).exists()
        if file_exist is True and file_name != '':
            messages.error(
                request, 'An error occured')
            return render(request, 'app_code_share/homepage.html', {})

        CodeShare.objects.create(code=code_share,
                                 hash_value=hash_value,
                                 file_name=file_name)
        return redirect('code_share:view_by_hash', hash_id=hash_value)


def view_by_hash(request, hash_id):
    """retrives the code snippet associated with the
    unique Hash anda handles the editing

    :param hash_id: unique ID of the code snippet

    GET:
        query database for code snippet

        :returns code snippet

    POST:
        handles updation in the content

        :param code_snippet: updated code snippet

        :returns redirects to this view again to render the new results

    """

    if request.method == 'GET':
        code_share = CodeShare.objects.get(hash_value=hash_id)
        context = {'code_share': code_share, "filename": "yes"}
        return render(request, 'app_code_share/homepage.html', context)

    if request.method == 'POST':
        code_share = request.POST.get('code_snippet')
        code_obj = goo404(CodeShare, hash_value=hash_id)
        code_obj.code = code_share
        code_obj.save()

        return redirect('code_share:view_by_hash', hash_id=hash_id)
