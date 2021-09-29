from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Category, Transaction, User, Wallet
# Create your views here.

def index(request):
    return render(request, "ledger/index.html")

def login_view(request):
    
    # Attempt to log user in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        # If authentication success
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "ledger/login.html", {
                "message": "Invalid username and/or password"
            })
    
    # Form to log user in
    else:
        return render(request, "ledger/login.html")
    
def logout_view(request):
    
    # Logs user out
    logout(request)
    return HttpResponseRedirect(reverse("index"))
        
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        
        # Ensures password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "ledger/register.html", {
                "message": "Passwords do not match"
            })

        # Attempts to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "ledger/register.html", {
                "message": "Username/Email already in used",
            })
        login(request, user)
        
        # Set default categories and wallet
        categories = [
            'Food',
            'Education',
            'Investment',
            'Utilites',
            'Other'
        ]
        
        for category in categories:
            set_category = Category(category=category, user=user)
            set_category.save()
        
        set_wallet = Wallet(name="Debit Card", owner=user)
        set_wallet.save()
        
        return HttpResponseRedirect(reverse("index"))
    
    else:
        return render(request, "ledger/register.html")
    
def new_transaction(request):
    if request.method == "GET":
        return render(request, "ledger/new_transaction.html")
    
def categories(request):
    if request.method == "GET":
        categories = Category.objects.filter(user=request.user)
        return render(request, "ledger/categories.html", {
            "categories": categories,
        })
    elif request.method == "POST":
        name = request.POST["category_name"]
        new_category = Category(category_name=name, user=request.user)
        new_category.save()
        return HttpResponseRedirect(reverse("categories"))
        
def wallets(request):
    if request.method == "GET":
        wallets = Wallet.objects.filter(owner=request.user)
        return render(request, "ledger/wallets.html", {
            "wallets": wallets,
        })