from django.shortcuts import render
from app.models import*
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETMFO=TopicModelform()
    d={'ETMFO':ETMFO}
    if request.method=='POST':
        ETMFO=TopicModelform (request.POST)
        if ETMFO.is_valid():
            ETMFO.save()

            return HttpResponse('topic model name is Successfully cretaed')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWMFO=WebpageModelform()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        EWMFO=WebpageModelform(request.POST)
        if EWMFO.is_valid():
            EWMFO.save()
            return HttpResponse('Webpage model name is Successfully created')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_webpage.html',d)  


def insert_accessrecord(request):
    EAMFO=AccessrecordModelform()
    d={'EAMFO':EAMFO}
    if request.method=='POST':
        EAMFO=AccessrecordModelform(request.POST)
        if EAMFO.is_valid():
            EAMFO.save()
            return HttpResponse('Accessrecord model name is Successfully created')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_accessrecord.html',d)  


def wish(request,name):
    return HttpResponse(f'{name} django frame work')




