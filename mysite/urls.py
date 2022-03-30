
from django.contrib import admin
from django.urls import re_path
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^',include('homepage.urls')),
   path('accounts/',include('allauth.urls')),
   
]
