from django.contrib.auth.models import User, Group
from django.db import models
from django.template.defaultfilters import slugify
from childcare import countries, themes
from utils.roles import roles_childcare_init_new
from utils.slugify import unique_slugify


class Childcare(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(verbose_name='URL, kindy.at/', unique=True, max_length=100)
    slogan = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = countries.CountryField()
    manager = models.ForeignKey(User, related_name='childcare_manager')
    employees = models.ManyToManyField(User, related_name='childcare_employees', blank=True)
    theme = themes.ThemeField(default='default')
    theme_image = models.CharField(max_length=100, blank=True, default='default')
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    #subscription
    #subscription_expires

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
            ('childcare_view', 'View childcare dashboard'),
            ('childcare_update', 'Updating childcare settings'),
            ('classroom_view', 'View classroom dashboard'),
        )

    def save(self, *args, **kwargs):
        is_create = False
        if not self.id:
            is_create = True

        if not self.slug:
            self.slug = unique_slugify(self, self.name)

        super(Childcare, self).save(*args, **kwargs)

        if is_create:
            roles_childcare_init_new(self)

    def get_absolute_url(self):
        return '/childcare/%s' % self.id


class GroupChildcare(models.Model):
    childcare = models.ForeignKey(Childcare)
    group = models.ForeignKey(Group)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.group.name

    class Meta:
        unique_together = ['childcare', 'group']


'''
class ChildcareNews(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    content = models.TextField()
    childcare = models.ForeignKey(Childcare)
    #images
    #documents/files

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/childcare/%s/news/%s' % (self.childcare.pk, self.pk)
'''


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    content = models.TextField()
    childcare = models.ForeignKey(Childcare)
    public = models.BooleanField(default=False)
    #images
    #documents/files

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            super(News, self).save(*args, **kwargs)

'''
class NewsComments(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    content = models.TextField()
    news = models.ForeignKey(News)

    def __unicode__(self):
        return self.content
'''