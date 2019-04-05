"""rafiproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
#from django.urls import path
from rafiapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('vinod', views.input),
    url('reg', views.reg),
    url('log/', views.log),
    #url('log/check/', views.check),
    url('output/',views.output),
   # url('input/',views.input),
    url('terms/',views.terms),
    url('feedback/',views.feedback),
    url('fback/',views.fback),
    url('image/',views.image),
    url('game/',views.game),
    url('gues/',views.gues),

]
