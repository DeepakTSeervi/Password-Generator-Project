from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, "generator/home.html")

def password(request):

    password_generated = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', '12'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_'))

    for x in range(length):
        password_generated += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password_generated })
    

