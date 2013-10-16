from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from registration.views import RegistrationView
from child.models import Child
from childcare.models import Childcare


def main(request):
    return render(request, 'kindy3/main.html')


# user profile site
#@login_required
def home(request):
    childcare_list = Childcare.objects.filter(manager=request.user)
    children_list = Child.objects.filter(guardians__id=request.user.id)
    return render(request, 'kindy3/home.html', {'childcare_list': childcare_list, 'children_list': children_list})