from django.shortcuts import render
from django.http import HttpResponse


def signup(request):
    return HttpResponse("<h1>Сторінка реєстарції</h1>")


def login(request):
    return HttpResponse("<h1>Сторінка входу</h1>")