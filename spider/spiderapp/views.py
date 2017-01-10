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

#ע��
def regist(request):
    if request.method =='POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #��ñ�����
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username=username,password=password)
            return HttpResponse('regist succees!!')
    else:
        uf = UserForm()
        #print RequestContext(request)
    return render_to_response('regist.html',{'uf':uf},context_instance=RequestContext(request))

                                  
#��½
def login(request):
    if request.method =='POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #��ȡ���û�����
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #��ȡ�ı�����������ݿ�Ƚ�
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #�Ƚϳɹ�,��תindex
                response = HttpResponseRedirect('spider/index')
                #��usernameд��cookie,ʧЧʱ��Ϊ3600
                response.set_cookie('username',username,3600)
                return response()
            else:
                #�Ƚ�ʧ�ܻ���login
                return HttpResponseRedirect('')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(request))
          
#��½�ɹ�
def index(request):
    username = request.COOKIES.get('username','')
    return render_to_response('index.html',{'username':username},context_instance=RequestContext(request))

#�˳�
def logout(request):
    response = HttpResponse('logout!!')
    #����cookie�ﱣ���username
    response.delete_cookie('username')
    return response






    
