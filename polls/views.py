from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
#from .forms import Info
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
#    form = Info()
    return render(request,"editar.html")

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('login_view')
