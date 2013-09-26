from django.contrib.auth.models import User
from django.db import models
from child.models import Child
from childcare.models import Childcare


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    childcare = models.ForeignKey(Childcare)
    teachers = models.ManyToManyField(User)


class ClassroomChildren(models.Model):
    child = models.ForeignKey(Child)
    classroom = models.ForeignKey(Classroom)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)