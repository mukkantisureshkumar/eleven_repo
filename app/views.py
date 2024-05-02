from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    tn=input('Enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    qlto=Topic.objects.all()
    d={'qlto':qlto}
    return render(request,'display_topic.html',d)

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
        wlto=Webpage.objects.all()
        d={'wlto':wlto}
        return render(request,'display_webpage.html',d)

    else:
        return HttpResponse('<marquee><h1>Given topic_name is not present in parent table</h1></marquee>')
    

def insert_accessrecord(request):
    i=int(input('Enter id:'))
    
    d=input('Enter date:')
    a=input('Enter author:')
    wo=Webpage.objects.get(id=i)
    a=AccessRecord.objects.get_or_create(name=wo,date=d,author=a)[0]
    a.save()
    #return HttpResponse('access is created')
    d={'key':AccessRecord.objects.all()}
    return render(request,'display_accessrecord.html',context=d)






def display_topic(request):
    qlto=Topic.objects.all()
    d={'qlto':qlto}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    wlto=Webpage.objects.all()
    wlto=Webpage.objects.all()[:5:]#slicing is possible
    wlto=Webpage.objects.filter(topic_name='cricket')
    wlto=Webpage.objects.exclude(topic_name='cricket')#except the condition satisfying data remaining all it fetch
    #ordering the data 
    wlto=Webpage.objects.all().order_by('name')#it gives ascending order of names by using accsi values
    wlto=Webpage.objects.order_by('-name')#if you are not providing the method all,filter & exclude it will take default as all() method [using hyphen - descending order]
    #we don't want to use accsi value but by using length of the characters we make ascending or descending for that we need to import Length function 
    from django.db.models.functions import Length
    wlto=Webpage.objects.order_by(Length('name'))#by default it display ascending order (less character)
    wlto=Webpage.objects.order_by(Length('name').desc())#by using  desc() method we can display name column in descending order 

    d={'wlto':wlto}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    alto=AccessRecord.objects.all()
    d={'key':alto}
    return render(request,'display_accessrecord.html',d)