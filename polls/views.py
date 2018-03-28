from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
#from .forms import UploadFileForm
from .forms import CargarArchivo
# Create your views here.


from django.http import HttpResponse

def index(request):
    form = AuthenticationForm()
    return render(request,'login_view.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request,user)
            return redirect('editar')
    else:
        form = AuthenticationForm()
    return render(request,'login_view.html',{'form':form})

@login_required(login_url="login")
def editar(request):
    if request.method =='POST':
        form = CargarArchivo(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,"Succesfully Created")
            return redirect('editar')
    else:
        form = CargarArchivo(request.POST, request.FILES)
    return render(request,"editar.html",{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('login_view')
"""
def upload_file(request):
    if request.method=='POST':
        form = uploadFileForm(request.POST,request.FILES)
        if form.is_valid():
        return redirect('login_view')
"""
