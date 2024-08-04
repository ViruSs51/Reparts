from django.shortcuts import render


def home(request):
    data = {}

    return render(request, "main-pages/home.html", data)
