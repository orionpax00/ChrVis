from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import string
import random

from . import handleupload
from . import generate_str
from .forms import DocumentForm

# Create your views here.
def homepage(request):
    return HttpResponse("<H1>I'm back to my bussiness</H1>")

def viewer(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.POST['password'] == '':
                password_ = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
            else:
                password_ = request.POST['password']
            user = User.Objects.create_user(request.POST['email'].split('@')[0],request.POST['email'],password_)
            user.save()
            generate_str.run_file()

            context = {
                'username' : request.POST['email'].split('@')[0],
                'password' : password_
            }
            return render(request,'job_submitted.html' ,context=context)
    else:
        form = DocumentForm()

        user_data = {
            'email':"dkumar@ce.iitr.ac.in"
        }
        handleupload.maketmplocation(user_data)
    return render(request, 'viewer.html',{'form':form})

def get_results(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['username'])

        if user is not None:
            ## do some thing good
            print("hello world")
        else:
            context = {
            'message': "Your username or password is wrong"
            }
            return render(request,'get_results.html',context=context)
    return render(request,'get_results.html')
