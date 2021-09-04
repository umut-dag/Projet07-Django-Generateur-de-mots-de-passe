from django.shortcuts import render
from django.http import HttpResponse
import random, string


def index(request):
    return render(request, 'app/index.html')

def password(request):
    
    all_chars = ""
    password = ""

    longueur = int(request.GET.get('longueur', 10))

    if request.GET.get('majuscules'):
        all_chars += string.ascii_uppercase
    if request.GET.get('minuscules'):
        all_chars += string.ascii_lowercase
    if request.GET.get('symboles'):
        all_chars += string.punctuation
    if request.GET.get('chiffres'):
        all_chars += string.digits

    for x in range (longueur):
        password += random.choice(all_chars)
        
    return render(request, 'app/password.html', {'password':password})