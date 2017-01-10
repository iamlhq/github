# -*- coding: cp936 -*-
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from blogapp.models import django

def date_now(request):
    context = {}
    context['now'] = datetime.datetime.now()
    return render(request,'date.html',context)


def date_(request,offset):
    context = {}
    offset = int(offset)
    context['offset'] = offset
    context['date_'] = datetime.datetime.now()+datetime.timedelta(hours=offset)
    return render(request,'date.html',context)

#���ݿ����
def testdb(request):
    test1 = django(name='abc')
    test1.save()
    return HttpResponse("<p>������ݳɹ�</p>")
    
    

#��ȡ����    
def testdb_get(request):
    #��ʼ��
    response = ""
    response1 = ""
    #ͨ��object���ģ�͹�������all()��ȡ���������У��൱��SQL�е�SELECT * FROM
    list = django.objects.all()
    #filter�൱��SQL�е�WHRER,�������������˽��
    response2 = django.objects.filter(id=1)

    #��ȡ��������
    response3 = django.objects.get(id=1)
    #���Ʒ��ص������൱��SQL�е�OFFSET 0 LIMIT 2
    django.objects.order_by('name')[0:2]

    #��������
    django.objects.order_by('id')

    #����ķ�����������ʹ��
    django.objects.filter(name='abc').order_by("id")

    #�����������
    for var in list:
        response1 += var.name+" "
    response = response1
    return HttpResponse('<p>'+response+'</p>')


#��������save update
def testdb_up(request):
    test1 = django.objects.get(id=1)
    test1.name = 'w3'
    # ����һ�ַ�ʽ
    #Test.objects.filter(id=1).update(name='w3cschool����̳�')
    # �޸����е���
    # Test.objects.all().update(name='w3cschool����̳�')
    test1.save()
    return HttpResponse("<p>�޸ĳɹ�</p>")


#ɾ������
def testdb_del(request):
    test1 = django.objects.get(id=1)
    test1.delete()
    # ����һ�ַ�ʽ
    # Test.objects.filter(id=1).delete()
	
    # ɾ����������
    # Test.objects.all().delete()
    return HttpResponse('<p>ɾ���ɹ�</p>')



    
















    
    
