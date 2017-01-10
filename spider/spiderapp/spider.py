# -*- coding: cp936 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
import requests


def download_page(request):
    urls = {}
    if 'MSG' in request.POST and request.POST['MSG']:
        msg = request.POST['MSG']
        urls = msg.split()
        return urls
    else:
        return urls











def get_url_text(request):
    urls=download_page(request)
    if urls:
        return render_to_response('result.html',{"urls":urls},context_instance=RequestContext(request))
    else:
        return HttpResponse(" no url please return and put in agin")
        
    
