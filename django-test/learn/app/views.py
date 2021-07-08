from django.shortcuts import render, redirect, HttpResponse
from . import models
from django.views.decorators import csrf



# Create your views here.

def test(request):
    return redirect("/hello/")


def login(request):
    status = request.COOKIES.get('is_login')
    if status:
        return redirect("/app/index/")
    if request.method == "GET":
        return render(request, "app/login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
    #print(user_obj.username)

    if not user_obj:
        return render(request,"app/login.html", {'msg': username + ' Error!'})
    else:
        rep = redirect("/app/index/")
        rep.set_cookie("is_login", True, path='/')
        return rep
       
def index(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    print(status)
    if not status:
        return redirect('/app/login/')
    return render(request, "app/index.html")

def logout(request):
    rep = redirect('/app/login/')
    rep.delete_cookie("is_login")
    return rep # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面
   
def order(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/app/login/')
    return render(request, "app/order.html")

def xx(request, year):
    print(year)
    return HttpResponse('xxxx---'+year)

def i(request):
    return render(request, "app/index.html")
