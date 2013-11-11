from django.contrib.auth.models import User
from django.db import models
from child.imagegenerators import GalleryThumbnail
from child.models import Child
from childcare.models import Childcare


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    childcare = models.ForeignKey(Childcare)
    teachers = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return 'childcare/%s/classroom/%s' % (self.childcare.pk, self.pk)


class Attendance(models.Model):
    author = models.ForeignKey(User)
    date = models.DateField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    classroom = models.ForeignKey(Classroom)
    attendance = models.ManyToManyField(Child)

    class Meta:
        unique_together = ['classroom', 'date']


class Diary(models.Model):
    author = models.ForeignKey(User)
    date = models.DateField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    classroom = models.ForeignKey(Classroom)
    content = models.TextField()

    class Meta:
        unique_together = ['classroom', 'date']


class DiaryImage(models.Model):
    image = models.ImageField(upload_to='images/childcare/')
    thumbnail = GalleryThumbnail(source='image')
    diary = models.ForeignKey(Diary)


class Plan(models.Model):
    author = models.ForeignKey(User)
    classrooms = models.ManyToManyField(Classroom)
    start_date = models.DateField()
    end_date = models.DateField()
    content = models.TextField()
    file = models.FileField(upload_to='files/plan/')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)