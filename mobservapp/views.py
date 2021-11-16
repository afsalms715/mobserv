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
    return render(request,'singup.html')
