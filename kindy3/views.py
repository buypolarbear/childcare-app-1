from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from childcare import models


def main(request):
    return render(request, 'kindy3/main.html')


# user profile site
@login_required
def home(request):
    childcares = models.Childcare.objects.filter(manager=request.user)
    return render(request, 'kindy3/home.html', {'childcares': childcares})