from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from . import handleupload
from .forms import DocumentForm

# Create your views here.
def homepage(request):
    return HttpResponse("<H1>I'm back to my bussiness</H1>")

def viewer(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()

        user_data = {
            'email':"dkumar@ce.iitr.ac.in"
        }
        handleupload.maketmplocation(user_data)
    return render(request, 'viewer.html',{'form':form})
