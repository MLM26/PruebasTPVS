from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Trader
from .forms import CargarArchivo
from django.utils import timezone
# Create your views here.


from django.http import HttpResponse


#Index
@login_required(login_url="login")
def index(request):
    return render(request,"index.html")


#Logs
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

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('login_view')




#Menu
@login_required(login_url="login")
def archivo(request):
    if request.method =='POST':
        form = CargarArchivo(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('archivo')
    else:
        form = CargarArchivo()
    return render(request,"archivo.html",{'form':form})

@login_required(login_url="login")
def contraparte(request):
    return render(request,"contraparte.html")

@login_required(login_url="login")
def estado(request):
    return render(request,"estado.html")

@login_required(login_url="login")
def portafolio(request):
    return render(request,"portafolio.html")


@login_required(login_url="login")
def producto(request):
    return render(request,"producto.html")

@login_required(login_url="login")
def trader(request):
    traders = Trader.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'trader.html', {'traders':traders})



@login_required(login_url="login")
def sistema(request):
    return render(request,"sistema.html")


