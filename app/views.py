from email import message
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
# from .filters import DjangoFilters


def main(request):
    dishes = Recipe.objects.all()
    context = {
        'dishes': dishes
    }
    # def get_context_data(self, **kwargs):
    #     context = super.get_context_data(**kwargs)
    #     context['filter'] = DjangoFilters(self.request.GET, queryset=self.get_queryset())
    #     return context
    
    return render(request, 'app/main.html', context)

def search(request):
    if request.method == 'GET':
        result = request.GET['query']
        dishes = Recipe.objects.filter(dish = result)
        context = {
            'dishes': dishes
        }
        return render(request, 'app/main.html', context)

def users_recipe(request):
    x = Recipe.objects.filter(user = request.user)
    context = {
        'data': x
    }
    print("HEy")
    return render(request, 'app/user_recipe.html', context)

def view_recipe(request, id):
    x = Recipe.objects.get(id = id)
    context = {
        'data': x
    }
    return render(request, 'app/view_recipe.html', context)

def update_recipe(request, id):
    x = Recipe.objects.get(id = id)
    context = {
        'data': x
    }
    if request.method == "POST":
        x.dish = request.POST.get('dish')
        x.ingredients = request.POST.get('ingredients')
        x.description = request.POST.get('description')
        if request.FILES['image']:
            x.image = request.FILES['image']
        x.save()
        return redirect('main')
    return render(request, 'app/update_recipe.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f"{username}, you  registered your account successfully!!")
            return redirect('login')
    context ={
        'form': form
    }
    return render(request, 'app/register.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            messages.info(request, "Username or Password is incorrect")
            
    return render(request, 'app/login_page.html')


def createrecipe(request):
    if request.method == 'POST':
        x = Recipe()
        x.user = request.user
        x.dish = request.POST.get('dish')
        x.ingredients = request.POST.get('ingredients')
        x.description = request.POST.get('description')
        x.image = request.FILES['image']
        x.save()
        return redirect('main')
    return render(request, 'app/createrecipe.html')


def logout_page(request):
    logout(request)
    return redirect('login')