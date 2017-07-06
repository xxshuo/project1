from django.conf.urls import patterns, include, url
from django.contrib import admin
from p1.views import *
from django.contrib.auth.views import *
from p1.v1 import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login$', login_v1),
    url(r'^accounts/login/$', login_v1),
    url(r'^login$', login_v1),
    url(r'^logout$', logout_v1),
    url(r'^change$', change_v1),
    url(r'^profile$',profile),
    #url(r'^t1$',t1),
    #url(r'^register$',register_v1),
    url(r'^check_user$',check_user),
    url(r'^check_code$',check_code),
    url(r'^upload/$',upload),
    url(r'^um_check$',um_check),
)
