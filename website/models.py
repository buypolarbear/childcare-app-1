from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
from django.db import models
from child.models import Child
from childcare.models import Childcare
from classroom.models import Classroom


class WebsiteNews(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    content = models.TextField()
    childcare = models.ForeignKey(Childcare)
    #TODO:images
    #TODO:files

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    #def get_absolute_url(self):
    #    return reverse('website.views.news_detail', args=[self.slug])


class EnrolledChildren(models.Model):
    child = models.ForeignKey(Child)
    childcare = models.ForeignKey(Childcare)
    classroom = models.ForeignKey(Classroom, null=True)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)