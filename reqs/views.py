from django.shortcuts import render, get_object_or_404,redirect

from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import View
from django.utils import timezone
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .render import Render
from .forms import SignUpForm
from .models import Project,File

class IndexView(generic.ListView):
    template_name='reqs/index.html'
    context_object_name='project_list'
    def get_queryset(self):
        return Project.objects.filter(creation_date__lte=timezone.now()).order_by('-creation_date')



class PdfView(View):
    
    def get(self,request, pk):
        selected_file=get_object_or_404(File,pk=pk)
        return Render.render(selected_file.formatted_markdown,
                            selected_file.file_name
                            )
        
    
   
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
