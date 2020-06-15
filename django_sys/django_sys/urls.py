"""django_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include
from login import views as views1
from game import views as views2
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name="index.html")),
    path('index/', TemplateView.as_view(template_name="index.html")),
    path('userInfo/', views1.index),  # To get the user level messag
    path('login/', views1.login),
    path('register/', views1.register),
    path('logout/', views1.logout),
    path('captcha/', include('captcha.urls')),
    path('confirm/', views1.user_confirm),
    path('game/', views2.game), #To get the final codelist
    path('mapInfo/', views2.map_info), #To get the map data
    path('mapEditor/', views2.map_editor) #Store the map data
]
