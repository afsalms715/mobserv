from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from . models import mobmsg,mobservices
from django.contrib import messages
# Create your views here.
def fun(request):
    obj=mobservices.objects.all()
    return render(request,'index.html',{'services':obj})

def message(request):
    email=request.POST['email']
    message=request.POST['message']
    print('email:'+email+'\n'+'message:'+message)
    msgs=mobmsg(email=email,msg=message)
    msgs.save()
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        print('name:'+name+'\n'+'email:'+email+'\n'+'password:'+password)
        if User.objects.filter(username=username).exists():
            messages.info(request,'user name already taken ')
            print("user name taken")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email is already taken ')
            print("email name taken")
            return redirect('signup')
        else:
            user=User.objects.create_user(username=username,password=password,email=email,first_name=name)
            user.save()
            print('create user')
            return redirect('/')
    else:
        return render(request,'singup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("succesfully ")
            return redirect('/')
        else:
            print('invalid critential')
            messages.info(request, 'invalid details')
            return redirect('login/')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

