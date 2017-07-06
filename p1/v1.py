#! usr/bin/python
#coding=utf-8
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from models import *
from admin import *
import datetime
import check_code as CheckCode
import os,json

static_url='http://192.168.137.131/'

def oo(request):
    print request.user
    up = User.objects.get(name=request.user)
    print '头像属性:',up.avatar
    return render_to_response('hello.html',
    {'avatar': up.avatar },context_instance=RequestContext(request))




def upload(request):
    if request.method == 'POST':
        ret = {'status': False, 'data': None, 'error': None}
        try:
            img = request.FILES.get('img')
	    if img.size <= 3048000:
            	f=open(os.path.join('/data/nginx/html/', img.name), 'wb+')
            	for chunk in img.chunks(chunk_size=1024):
                	f.write(chunk)
            	ret['status'] = True
            	ret['data'] = os.path.join('/data/nginx/html/', img.name)
	    	f.close()
		url=static_url + img.name
		up = User.objects.get(name=request.user)
		up.avatar = url
		up.save()
	    	print request.user,img,img.size,ret,'http://193.168.137.131/%s'%img.name
	        	
			 
	    else:
		ret['status'] = False
		ret['data'] = '文件过大'
	    	print request.user,img,img.size,ret
        except Exception as e:
            ret['error'] = e
        finally:
            return HttpResponse(json.dumps(ret))
    return render(request, 'hello.html')
