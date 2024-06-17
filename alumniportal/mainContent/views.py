from django.shortcuts import render, HttpResponse
from .forms import FormWithCaptcha

# Create your views here.
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def index(request):
    context = {'form' : FormWithCaptcha()}
    return render(request, 'index.html', context)
