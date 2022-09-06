from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import *
from .forms import *


# Index Page
def index(request):
    return render(request, 'main.html')


def registerUser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

            userMessage = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + userMessage)

            # don't need to create the empty object. We will set route to create/update/delete objects later on
            #StockInfo.objects.create(
            #    user=user,
            #)

            return redirect('users:loginuser')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'registration/registerUser.html', context)

#Login User
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username') # we get this from the form (loginuser.html) input name=""
        password = request.POST.get('password') # we get this from the form (loginuser.html) input password=""

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:index')
        else:
            messages.info(request, 'Username OR password is incorrect') # flash a message

    context = {}
    return render(request, 'accounts/loginuser.html', context)

# Logout User Page (no template needed)
def logoutUser(request):
    logout(request)
    return redirect('users:loginuser')

# Report Page
@login_required(login_url='users:loginuser')
def report(request):
    stock_info = StockInfo.objects.all()

    totalStockInfo = stock_info.count()

    context = {
        'stock_info': stock_info,
        'totalStockInfo': totalStockInfo
    }

    return render(request, 'accounts/report.html', context)
