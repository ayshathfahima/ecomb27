from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .models import Product

#Object Relational MApping

def home(request):
    product=Product.objects.all()
    print(product)
    return render(request,'home.html',{'product':product})
def add_product(request):
    if request.method=='POST':
        productform=ProductForm(request.POST,request.FILES)
        if productform.is_valid():
            productform.save()
    productform=ProductForm()
    return render(request,'add_product.html',{'form':productform})

def edit_product(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    if request.method=='POST':
        product_form=ProductForm(request.POST,request.FILES,instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')
    product_form=ProductForm(instance=product)
    return render(request,'edit_product.html',{'form':product_form})


def delete_product(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('home')


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']

        myuser= User.objects.create_user(username=username,password=password1,email=email)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('signin')
    return render(request,'signup.html')


def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            lname=user.last_name
            return render(request,'user_dashboard.html',{'fname':fname,'lname':lname})
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('signin')

    return render(request,'signin.html')

def signout(request):
    logout(request)
    return render(request,'home.html')


