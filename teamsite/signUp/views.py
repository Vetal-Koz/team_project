from django.shortcuts import render
from django.http import HttpResponse


def signup(request):
    return render(request, 'signUp/sign_up.html')


def login(request):
    return HttpResponse("<h1>Сторінка входу</h1>")