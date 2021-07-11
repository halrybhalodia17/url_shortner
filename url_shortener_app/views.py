from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import URLForm, loginform
from .models import LongToShort

import secrets
import datetime



def home(request):
    return render(request, 'home.html',)

def login(request):
    if request.method == 'POST':
        userform = loginform(request.POST)
        ip_email= userform.data['email']
        ip_password = userform.data['password']
        if ip_email == "myproject@gmail.com" and ip_password =="password":
            return redirect('/analytics')
        else:
            return HttpResponse("Your email or password is wrong")
    else:
        myform = loginform()
        return render(request, 'login.html', {'form': myform})

def shorten(request):
    if request.method == 'POST':
        userform = URLForm(request.POST)
        ip_longurl = userform.data['longurl']
        ip_customname = userform.data['customname']
        ip_date = datetime.datetime.now()
        if (ip_customname == ""):
            ip_shorturl = secrets.token_hex(3)
            final_url = ip_shorturl
            obj =LongToShort(longurl=ip_longurl, shorturl=ip_shorturl,Date = ip_date)
        else:
            entries = LongToShort.objects.filter(shorturl = ip_customname)
            if len(entries) == 0:
                final_url = ip_customname
                obj = LongToShort(longurl = ip_longurl, shorturl = ip_customname,Date = ip_date)
            else:
                return HttpResponse('Sorry. The custom name is already taken.') 
        obj.save()
        return HttpResponse('Your shorturl is: ' + 'http://localhost:8000/redirect/' + final_url)
    else:
        myform = URLForm()
        return render(request, 'form.html', {'form': myform})

def redirect_url(request, link):
    try:
        obj = LongToShort.objects.get(shorturl = link)
        req_longurl = obj.longurl
        obj.visit_count += 1

        obj.save()
        return redirect(req_longurl)
    except Exception as e:
        print(e)
        return HttpResponse('Invalid short url.')
    
def get_analytics(request):
    rows = LongToShort.objects.all()
    return render(request, 'analytics.html', {'data': rows})