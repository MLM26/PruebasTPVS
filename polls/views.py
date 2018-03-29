from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
#from .forms import UploadFileForm
from .forms import CargarArchivo
# Create your views here.


from django.http import HttpResponse

@login_required(login_url="login")
def index(request):
    return render(request,"index.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request,'login_view.html',{'form':form})

@login_required(login_url="login")
def archivo(request):
    if request.method =='POST':
        form = CargarArchivo(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,"Succesfully Created")
            return redirect('archivo')
    else:
        form = CargarArchivo()
    return render(request,"archivo.html",{'form':form})

@login_required(login_url="login")
def traders(request):
    return render(request,"traders.html")

@login_required(login_url="login")
def sistemas(request):
    return render(request,"sistemas.html")

@login_required(login_url="login")
def portafolios(request):
    return render(request,"portafolios.html")

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('login_view')
