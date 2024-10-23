from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.utils.safestring import mark_safe
from .forms import LoginForm

# Create your views here.
def redirect_login(request):
    return redirect('login')

def user_login(request):
    data = {
        'message_data': {
            'title': 'Message'
        }
    }

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    data['message_data']['message'] = mark_safe('<span class="green">Успешная аутентификация!</span>')

                    return render(request, 'authentication/message.html', data)
                else:
                    data['message_data']['message'] = mark_safe('<span class="red">Учетная запись отключена.</span>')

                    return render(request, 'authentication/message.html', data)
            else:
                data['message_data']['message'] = mark_safe('<span class="red">Неверный логин или пароль.</span>')

                return render(request, 'authentication/message.html', data)
        
    else:
        form = LoginForm()

    data['form'] = form

    return render(request, 'authentication/login.html', data)

def user_signup(request):
    data = {}

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        pass

    return render(request, 'authentication/signup.html', data)

def user_logout(request):
    data = {}

    if request.user.is_authenticated:
        logout(request)
        data['user_connected'] = request.user.is_authenticated
        data['message_data'] = {
            'title': 'Logged out',
            'message': mark_safe(f'You have been successfully logged out. You can <a href="{reverse("login")}">log-in again</a>.')
        }
    else:
        return redirect('home')

    return render(request, 'authentication/message.html', data)