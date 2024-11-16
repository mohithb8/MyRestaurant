from django.shortcuts import render,redirect
from dinner.models import Menu
from django.conf import settings
from django.conf.urls.static import static
# Create your views here.

def home(request):
    return render(request,'nav.html')



def menu(request):
    result= Menu.objects.all()
    print(settings.MEDIA_ROOT)
    if request.method=="POST":
        #result= Menu.objects.all()
        return render(request,'menu.html',{'res':result})
    else:
        return render(request,'menu.html',{'res':result})


def fun1(request):
    result=Menu.objects.all()
    if request.method=="POST":
        dish=request.POST.get("food")
        cost=request.POST.get("price")
        image=request.POST.get("image")
        obj=Menu(item=dish,price=cost)
        obj.save()
        result=Menu.objects.all()
        return render(request,"food.html",{"res":result , "obj":obj})
    return render(request,"food.html")