from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'hello world'
    context['welcome'] = 'welcome lhq'
    return render(request,'hello.html',context)


