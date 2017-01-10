from django.conf.urls import patterns,url
import views
import spider

urlpatterns = patterns('',
    url(r'^$',views.login,name = 'login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
    url(r'^get_url_text/$',spider.get_url_text,name = 'get_url_text'),
    )
