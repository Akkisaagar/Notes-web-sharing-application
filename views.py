from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date
from django.http import HttpResponse
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def faq(request):
    return render(request,'faq.html')
def privacypolicy(request):
    return render(request,'privacypolicy.html')
def copyright(request):
    return render(request,'copyright.html')
def refundpolicy(request):
    return render(request,'refundpolicy.html')
def Termsofuse(request):
    return render(request,'Termsofuse.html')
def user_login(request):
 error= " "
 if request.method == 'POST':
        e = request.POST['name']
        p = request.POST['pwd']
        
        user = authenticate(username=e,password=p)
        print(user)
        try:
            if user:
                login(request, user)
                print('Login Successfully')
                error = "no"
                d = {'error': error}
                return render(request,'profile.html', d)
            else:
                error = "yes"
        except:
            error = "yes"
 d = {'error': error}
 return render(request,'user_login.html', d)
def admin_login(request):
    error= " "
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error="no"
            else:
                error= "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'admin_login.html',d)

def signup1(request):
    error=""
    if request.method == 'POST':
        f = request.POST['fname']
        m = request.POST['mname']
        l = request.POST['lname']
        e = request.POST['emailid']
        c = request.POST['contact']
        p = request.POST['pwd']
        y = request.POST['year']
        s = request.POST['stream']
        t = request.POST['role']
        r = request.POST['roll']
        u=User.objects.create(username=f+l,first_name=f,last_name=l,email=e,password=p)
        Signup.objects.create(user=u,contact=c,year=y,stream=s,role=t,roll=r)
        print(u)
        return  HttpResponse('Data is collected')
    d = {'error': error}
    return render(request,'signup1.html', d)
def admin_home(request):
    if  not request.user.is_staff:
        return redirect('admin_login')
    pn = Notes.objects.filter(status="pending").count()
    an = Notes.objects.filter(status="accepted").count()
    rn = Notes.objects.filter(status="rejected").count()
    alln = Notes.objects.all().count()
    d = {'pn':pn,'an':an,'rn':rn,'alln':alln}
    return render(request,'admin_home.html',d)
def admin_logout(request):
     logout(request)
     return redirect('index')
def profile(request):
    if  not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    d = {'data':data,'user':user}
    return render(request,'profile.html',d)

def changepassword(request):
    error=""
    if  not request.user.is_authenticated:
        return redirect('user_login')
    if request.method=="POST":
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if c==n:
            u = User.object.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error="no"
        else:
            error="yes"
    d={'error':error}
    return render(request,'changepassword.html',d)
def edit_profile(request):
    if  not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    error = False
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        y = request.POST['year']
        s = request.POST['stream']
        r = request.POST['roll']
        user.first_name = f
        user.last_name = l
        data.roll = r
        data.contact = c
        data.stream = s
        data.year = y
        user.save()
        data.save()
        error=True
        
    d = {'data':data,'user':user, 'error':error}
    return render(request,'edit_profile.html',d)
def uploadnotes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method=='POST':
        b = request.POST['stream']
        y = request.POST['year']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['description']
        u = User.objects.filter(username=request.user.username).first()
    try:
       Notes.objects.create(user=u,uploadingdate=date.today(),stream=b,subject=s,year=y,notesfile=n,filetype=f,description=d,status='pending')
       error="no"
    except:
        error="yes"
        d={'error':error}
    return render(request,'uploadnotes.html',d)
def viewusers(request):
    if  not request.user.is_authenticated:
        return redirect('admin_login')
    users = Signup.objects.all()
    d = {'users':users}
    return render(request,'viewusers.html',d)
def viewnotes(request):
    if  not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user=user)
        
    d = {'notes':notes}
    return render(request,'viewnotes.html',d)
def delete_mynotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes= Notes.objects.get(id=pid)
    notes.delete()
    return redirect('viewnotes')
def delete_users(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user= User.objects.get(id=pid)
    user.delete()
    return redirect('viewusers')
def pending(request):
    if  not request.user.is_authenticated:
        return redirect('admin_login')
    notes = Notes.objects.filter(status="pending")
    d = {'notes':notes}
    return render(request,'pending.html',d)
def accepted(request):
    if  not request.user.is_authenticated:
        return redirect('admin_login')
    notes = Notes.objects.filter(status="accepted")
    d = {'notes':notes}
    return render(request,'accepted.html',d)
def rejected(request):
    if  not request.user.is_authenticated:
        return redirect('admin_login')
    notes = Notes.objects.filter(status="rejected")
    d = {'notes':notes}
    return render(request,'rejected.html',d)
def allnotes(request):
    if  not request.user.is_authenticated:
        return redirect('admin_login')
    notes = Notes.objects.all()
    d = {'notes':notes}
    return render(request,'allnotes.html',d)
def assignstatus(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    notes= Notes.objects.get(id=pid)
    error = ""
    if request.method =='POST':
        s = request.POST['status']
        try:
            notes.status= s
            notes.save()
            error="no"
        except:
          error="yes"
    d = {'notes':notes, 'error': error}
    return render (request,'assignstatus.html',d)
def delete_notes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes= Notes.objects.get(id=pid)
    notes.delete()
    return redirect('allnotes')
def viewallnotes(request):
    if  not request.user.is_authenticated:
        return redirect('user_login')
    notes = Notes.objects.filter(status="accepted")
    d = {'notes':notes}
    return render(request,'viewallnotes.html',d)