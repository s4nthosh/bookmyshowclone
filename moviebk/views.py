from django.shortcuts import render,redirect
from .models import *

def home (request):
    banner= movies.objects.filter(name='recommended')
    rec=list_mov.objects.filter(movie__name='recommended')
    banner1= movies.objects.filter(name='premier')
    rec_p=list_mov.objects.filter(movie__name='premier')
    context={'banner':banner,'rec':rec,'banner1':banner1,'rec_p':rec_p}
    return render(request,'index.html',context)


def nxt(request,name):
    if(list_mov.objects.filter(name=name)):
        nxtpage=main.objects.filter(movie__name=name)
        cast=cast_crew.objects.filter(movie__name=name)
        context={"nxtpage":nxtpage,"cast":cast}
        return render(request,'aboutbking.html',context)
    else:
        return redirect('index.html')
    

def theaterbk(request,name):
    if(theaters.objects.filter(movie__name=name,)):
        bk=theaters.objects.filter(movie__name=name)
        sa=list_mov.objects.filter(name=name)
        time=date_time.objects.filter(movie__name=name)
        context={"bk":bk,"sa":sa,"time":time,}
        return render(request,'theaters.html',context)
    else:
        return redirect('nxt')
    
def bookings(request,name,theater,time):
    if(date_time.objects.filter(movie__name=name)):
        tk=seats.objects.all()
        sk=(name,theater,time)
        context={"tk":tk,"sk":sk,}
        return render(request,'booking.html',context)
    else:
        return redirect('home')

def confbk(request):
        return render(request,'conf.html')