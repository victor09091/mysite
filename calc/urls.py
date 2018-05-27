from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

#urlpatterns = patterns('',
#    # 注意下面这一行
#    url(r'^$', 'tools.views.index', name='home'),
#    url(r'^admin/', include(admin.site.urls)),
#)