#from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import login
from django.conf.urls import url, include
#from django.conf import settings
#from django.conf.urls.static import static
from .import views


urlpatterns = [
    url(r'^$',views.login_view,name="login_view"),
    url(r'^editar/',views.editar,name="editar"),
    url(r'^login/$',views.login_view,name="login"),
    url(r'^logout/$',views.logout_view,name="logout"),
#    url(r'^logout$',views.login_view,name="login_view")
]

"""
if settings.DEBUG:
        urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
