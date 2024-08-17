from django.shortcuts import render


def home(request):
    data = {
        'page': 'home'
    }

    return render(request, "main-pages/home.html", data)
