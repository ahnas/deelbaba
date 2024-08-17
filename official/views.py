from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('official:home'))
        else:
            context = {
                "is_login": False,
                "error_message": "Invalid username or password",
            }
            return render(request, 'official/login.html', context)
    else:
        context = {
            "is_login": True,
        }
        return render(request, 'official/login.html', context)
    
def logout_view(request):
    logout(request)
    return redirect(reverse('official:login'))

@login_required
def home(request):
    products = Product.objects.all()
    context = {
        "is_product": True,
        "products": products,
        "username": request.user.username,
    }
    return render(request, 'official/home.html',context)
