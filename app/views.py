from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    tn=input('Enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('<center><h1>topic is created</h1></center>')

def insert_webpage(request):
    tn=input('Enter topic_name:')
    n=input('Enter name:')
    url=input('Enter url:')
    email=input('Enter email:')
    TO=Topic.objects.filter(topic_name=tn)
    if TO:
        kto=TO[0]
        w=Webpage.objects.get_or_create(topic_name=kto,name=n,url=url,email=email)[0]
        w.save()
        return HttpResponse('<center><h1>webpage is created</h1></center>')
    else:
        return HttpResponse('<marquee><h1>Given topic_name is not present in parent table</h1></marquee>')
    


def display_topic(request):
    qlto=Topic.objects.all()
    d={'qlto':qlto}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    wlto=Webpage.objects.all()
    d={'wlto':wlto}
    return render(request,'display_webpage.html',d)
































def insert_accessrecord(request):
    tn=input('Enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()

    n=input('Enter name:')
    url=input('Enter url:')
    email=input('Enter email:')
    w=Webpage.objects.get_or_create(topic_name=to,name=n,url=url,email=email)[0]
    w.save()  

    d=input('Enter date:')
    a=input('Enter author:')
    a=AccessRecord.objects.get_or_create(name=w,date=d,author=a)[0]
    a.save()

    return HttpResponse('<center><h1>Access Is Created</h1></center>')
