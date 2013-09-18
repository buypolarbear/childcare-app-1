from django.shortcuts import render


def home(request):
    return render(request, 'kindy3/main.html')