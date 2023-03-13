from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as logIn
from django.http import HttpResponse
from .forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email='email', password='password')
            logIn(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signUp/sign_up.html', {
        'form': form,
    })


def login(request):
    error = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            logIn(request, user)
            return redirect('home')
        else:
            error = 'Invalid email or password'
            messages.error(request, 'Please enter a correct email and password.')

    data = {
        'error': error,
    }
    return render(request, 'signUp/login1.html', data)