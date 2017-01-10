"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from view import date_now
from view import date_
from view import testdb
from view import testdb_get,testdb_up,testdb_del
urlpatterns = patterns('',
    (r'^date_now/',date_now),
    (r'^date_/(\d+)/$',date_),
    (r'^testdb/',testdb),
    (r'^testdb_get/',testdb_get),
    (r'^testdb_up/',testdb_up),
    (r'^testdb_del/',testdb_del),
                       
)



