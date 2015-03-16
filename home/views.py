from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404

from .models import PageViews

# Create your views here.
def index(request):
    p_view = PageViews()
    p_view.no_views += 1
    print p_view.no_views
    p_view.save()
    return render(request, 'home/index.html', {'page_views' : p_view.no_views})

def resume(request):
    file_name = 'resume.pdf'
    f = open('home/static/home/{}'.format(file_name), 'rb')
    response = HttpResponse(f, content_type='application/pdf')

    # Uncomment the below line to download the file instead of viewing it in the browser.
    #response['Content-Disposition'] = "attachment; filename={}".format(file_name)
    return response

def projects(request):
    return render(request, 'home/projects.html')

def contact(request):
    return render(request, 'home/contact.html')

