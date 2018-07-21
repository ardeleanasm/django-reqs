from django.shortcuts import render, get_object_or_404,redirect

from .models import Project
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Project,File
from .forms import SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm


class IndexView(generic.ListView):
    template_name='reqs/index.html'
    context_object_name='project_list'
    def get_queryset(self):
        return Project.objects.filter(creation_date__lte=timezone.now()).order_by('-creation_date')

class DetailView(generic.DetailView):
    model = Project
    template_name='reqs/detail.html'
    def get_queryset(self):
        return Project.objects.filter(creation_date__lte=timezone.now())


class FileView(generic.DetailView):
    model=File
    template_name='reqs/file_detail.html'
    def get_queryset(self):
        return File.objects.filter(creation_date__lte=timezone.now())    
    

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('../')
    else:
        form=SignUpForm()
    return render(request,'reqs/signup.html',{'form':form})


def reqs_logout(request):
    logout(request)
    return redirect('../')
