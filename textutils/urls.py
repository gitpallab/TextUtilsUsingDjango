"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome',views.welcome,name='welcome'),
    path('aboutBabes',views.aboutBabes,name='aboutBeb'),
    path('showFile',views.showFile,name='fileContent'),
    path('',views.index,name='index'),

    path('removePunc',views.removePunc,name='removePunc'),
    path('capFirst',views.capFirst,name='capFirst'),
    path('removeNewLine',views.removeNewLine,name='removeNewLine'),
    path('removeSpace',views.removeSpace,name='removeSpace'),
    path('countChar',views.countChar,name='countChar'),

    path('analyser',views.analyser,name='analyser'),
]
