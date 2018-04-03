#from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import login
from django.conf.urls import url, include
#from django.conf import settings
#from django.conf.urls.static import static
from .import views


urlpatterns = [
    url(r'^login',views.login_view,name="login_view"),
    url(r'^index',views.index,name="index"),
    url(r'^archivo/',views.archivo,name="archivo"),
    url(r'^logout/$',views.logout_view,name="logout"),
    url(r'^traders/$',views.traders,name="traders"),
    url(r'^sistemas/$',views.sistemas,name="sistemas"),
    url(r'^portafolios/$',views.portafolios,name="portafolios"),
    url(r'^producto/$',views.producto,name="productos"),
#    url(r'^logout$',views.login_view,name="login_view")
]

"""
if settings.DEBUG:
        urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
