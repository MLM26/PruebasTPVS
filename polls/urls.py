#from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import login
from .import views

urlpatterns = [
    url(r'^$',views.login_view,name="login_view"),
    url(r'^editar/',views.editar,name="editar"),
    url(r'^login/$',views.login_view,name="login"),
    url(r'^logout/$',views.logout_view,name="logout"),
#    url(r'^logout$',views.login_view,name="login_view")
]
