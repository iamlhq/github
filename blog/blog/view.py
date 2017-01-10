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

#数据库操作
def testdb(request):
    test1 = django(name='abc')
    test1.save()
    return HttpResponse("<p>添加数据成功</p>")
    
    

#获取数据    
def testdb_get(request):
    #初始化
    response = ""
    response1 = ""
    #通过object这个模型管理器的all()获取所有数据行，相当于SQL中的SELECT * FROM
    list = django.objects.all()
    #filter相当于SQL中的WHRER,可设置条件过滤结果
    response2 = django.objects.filter(id=1)

    #获取单个对象
    response3 = django.objects.get(id=1)
    #限制返回的数据相当于SQL中的OFFSET 0 LIMIT 2
    django.objects.order_by('name')[0:2]

    #数据排序
    django.objects.order_by('id')

    #上面的方法可以连锁使用
    django.objects.filter(name='abc').order_by("id")

    #输出所有数据
    for var in list:
        response1 += var.name+" "
    response = response1
    return HttpResponse('<p>'+response+'</p>')


#更新数据save update
def testdb_up(request):
    test1 = django.objects.get(id=1)
    test1.name = 'w3'
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='w3cschool菜鸟教程')
    # 修改所有的列
    # Test.objects.all().update(name='w3cschool菜鸟教程')
    test1.save()
    return HttpResponse("<p>修改成功</p>")


#删除数据
def testdb_del(request):
    test1 = django.objects.get(id=1)
    test1.delete()
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
	
    # 删除所有数据
    # Test.objects.all().delete()
    return HttpResponse('<p>删除成功</p>')



    
















    
    
