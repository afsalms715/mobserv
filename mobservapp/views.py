from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from . models import mobmsg
# Create your views here.
def fun(request):
    obj=mobmsg.objects.all()
    return render(request,'index.html')

def messages(request):
    email=request.POST['email']
    message=request.POST['message']
    print('email:'+email+'\n'+'message:'+message)
    msgs=mobmsg(email=email,msg=message)
    msgs.save()
    return redirect('/')
def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        print('name:'+name+'\n'+'email:'+email+'\n'+'password:'+password)
        user=User.objects.create_user(username=username,password=password,email=email,first_name=name)
        user.save()
        print('create user')
        return redirect('/')
    return render(request,'singup.html')
