from django.shortcuts import render, redirect

# Create your views here.
def auth_redirect(request):
    return redirect('login')

def login(request):
    data = {}

    return render(request, 'authentication/login.html', data)

def signup(request):
    data = {}

    return render(request, 'authentication/signup.html', data)