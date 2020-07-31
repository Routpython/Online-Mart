from django.shortcuts import render,redirect
from django.contrib import  messages
from app1.models import Productdetails,Usermodel
from django.core.paginator import Paginator


def index(request):
    pro=Productdetails.objects.all()
    p1=Paginator(pro,2)
    page_number=request.GET.get("page_no",1)
    page=p1.page(page_number)
    length=len(page)

    return render(request,"index.html",{"data":page,"baya":page_number,"length":length})
def admi1(request):
    return render(request,"admin.html")
def adlogin(request):
    uname=request.POST.get('t1')
    passw=request.POST.get('t2')
    un="BAPUJI"
    if uname == "bapuji" and passw == "bapuji":
        return render(request,"adminhome.html",{"data":un})
    else:
        return render(request,"admin.html",{"msg":"Check Username and Password"})

def adminhome(request):
    un = "BAPUJI"
    return render(request,"adminhome.html",{"data":un})
def adminuser(request):
    user=Usermodel.objects.all()
    p2=Paginator(user,1)
    page_number=request.GET.get("page_no",1)

    page=p2.page(page_number)

    return render(request,"adminuser.html",{"data":page})
def uslogin(request):
    return render(request,"uslogin.html")

def adminproduct(request):
    res = Productdetails.objects.all()
    p2=Paginator(res,2)
    page_number=request.GET.get("page_no",1)
    page=p2.page(page_number)
    return render(request, "adminproduct.html", {"data":page})


def addproduct(request):
    name=request.POST.get('p1')
    price=request.POST.get('p2')
    quan=request.POST.get('p3')
    image=request.FILES['p4']
    status="active"
    Productdetails(pname=name,price=price,quantity=quan,image=image,status=status).save()
    return redirect('adminproduct')
def pupdate(request):
    id=request.GET.get('no')
    res=Productdetails.objects.get(idno=id)
    return render(request,"product_update.html",{"data":res})

def register(request):
    return render(request, "register.html")

def register_user(request):
    name = request.POST.get('t1')
    contact = request.POST.get('t2')
    email = request.POST.get('t3')
    passw = request.POST.get('t4')
    status = 'pending'
    Usermodel(name=name, contact=contact, email=email, password=passw, status=status).save()
    messages.success(request,'Message saved Successfully')
    return redirect('register')


def user_login(request):
    un= request.POST.get('t1')
    pasw=request.POST.get('t2')
    Usermodel.objects.get(name=un,password=pasw)
    return render(request,"ushome.html",{"name":un,})


def userhome(request):
    uname=request.GET.get("un")
    user = Usermodel.objects.get(name=uname)

    return render(request,"ushome.html",{"name":uname,"data":user})


def user_update(request):
    uname = request.GET.get("un")
    user = Usermodel.objects.get(name=uname)

    return render(request,"user_update.html",{"name":uname,"data":user})


def save_update(request):
    id=request.POST.get('t1')
    name = request.POST.get('t2')
    contact = request.POST.get('t3')
    email = request.POST.get('t4')
    passw = request.POST.get('t5')
    Usermodel.objects.filter(no=id,contact=contact).update(name=name,email=email,password=passw)
    return render(request,"user_update.html",{"name":name})


def pro_update_save(request):
    id=request.POST.get('t1')
    name = request.POST.get('t2')
    price = request.POST.get('t3')
    quan = request.POST.get('t4')
    image = request.FILES['t5']

    Productdetails.objects.filter(idno=id).update(pname=name,price=price,quantity=quan,image=image)

    return redirect('adminproduct')


def pro_delete(request):
    idno=request.GET.get('no')
    Productdetails.objects.filter(idno=idno).delete()
    return redirect('adminproduct')