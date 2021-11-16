from django.shortcuts import render
from . models import mobmsg
# Create your views here.
def fun(request):
    obj=mobmsg.objects.all()
    return render(request,'index.html')