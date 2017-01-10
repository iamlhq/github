# -*- coding: cp936 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "spider.settings"})

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

#注册
def regist(request):
    if request.method =='POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username=username,password=password)
            return HttpResponse('regist succees!!')
    else:
        uf = UserForm()
        #print RequestContext(request)
    return render_to_response('regist.html',{'uf':uf},context_instance=RequestContext(request))

                                  
#登陆
def login(request):
    if request.method =='POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与表单数据库比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功,挑转index
                response = HttpResponseRedirect('spider/index')
                #将username写入cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response()
            else:
                #比较失败还在login
                return HttpResponseRedirect('')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(request))
          
#登陆成功
def index(request):
    username = request.COOKIES.get('username','')
    return render_to_response('index.html',{'username':username},context_instance=RequestContext(request))

#退出
def logout(request):
    response = HttpResponse('logout!!')
    #清理cookie里保存的username
    response.delete_cookie('username')
    return response






    
