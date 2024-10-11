from django.shortcuts import render

# Create your views here.
def home(request):
    data = {}

    return render(request, 'main/home.html', data)