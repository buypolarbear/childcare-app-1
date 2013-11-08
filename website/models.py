from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from child.models import Child
from childcare.models import Childcare
from classroom.models import Classroom


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    content = models.TextField()
    childcare = models.ForeignKey(Childcare)
    order = models.SmallIntegerField(default=1)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            super(Page, self).save(*args, **kwargs)


class PageFile(models.Model):
    file = models.FileField(upload_to='files/page/')
    description = models.CharField(max_length=500, blank=True)
    uploader = models.ForeignKey(User)
    page = models.ForeignKey(Page)
    created = models.DateTimeField(auto_now_add=True)


class EnrolledChild(models.Model):
    child = models.ForeignKey(Child)
    childcare = models.ForeignKey(Childcare)
    classroom = models.ForeignKey(Classroom, null=True)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['child', 'childcare']

    def __unicode__(self):
        return self.child