from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpRequest
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from models import *


def render_response(request, template, data=None):
    data = data or {}  
    r = RequestContext(request)
    data['ref_path'] = request.get_full_path()
    return render_to_response(template, data, context_instance=r)

def home(request):
	response_data 	= News.objects.all()
	main_news   	= response_data[0]
	section_2   	= response_data[1:3] 
	section_3   	= response_data[3:5]
	section_4   	= response_data[6]
	section_5   	= response_data[5:9]
	all_news    	= response_data
	reviews		= Movie_review.objects.all() 
	return render_to_response('home.html', {'news_1' : main_news,
						'section_2' : section_2,
						'section_3' : section_3,
						'section_4' : section_4,
						'section_5' : section_5,
						'all_news'  : all_news,
						'rows'	    : [1,2,3]})
