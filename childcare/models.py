from django.contrib.auth.models import User, Group
from django.db import models
from django.template.defaultfilters import slugify
from childcare import countries, themes, subscriptions
from utils.roles import roles_childcare_init_new
from utils.slugify import unique_slugify
from datetime import datetime, timedelta
from child.imagegenerators import GalleryThumbnail
from localflavor.us import models as usmodels


def one_month_trial():
    return datetime.now() + timedelta(days=30)


class Childcare(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(verbose_name='URL: kindy.at/', unique=True, max_length=100)
    logo = models.ImageField(upload_to='images/logos/', blank=True)
    slogan = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = usmodels.USStateField(blank=True)
    country = countries.CountryField()
    manager = models.ForeignKey(User, related_name='childcare_manager')
    employees = models.ManyToManyField(User, related_name='childcare_employees', blank=True)
    theme = themes.ThemeField(default='default')
    theme_image = models.CharField(max_length=100, blank=True, default='default')
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    subscription = subscriptions.SubscriptionField(default='trial')
    subscription_expires = models.DateTimeField(default=one_month_trial())
    disabled = models.BooleanField(default=False)

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


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    content = models.TextField()
    childcare = models.ForeignKey(Childcare)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            super(News, self).save(*args, **kwargs)


class NewsImage(models.Model):
    image = models.ImageField(upload_to='images/news/', blank=True)
    news = models.ForeignKey(News)
    thumbnail = GalleryThumbnail(source='image')


class NewsFile(models.Model):
    file = models.FileField(upload_to='files/news/')
    description = models.CharField(max_length=500, blank=True)
    uploader = models.ForeignKey(User)
    news = models.ForeignKey(News)


'''
class NewsComment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    content = models.TextField()
    news = models.ForeignKey(News)
'''


class Task(models.Model):
    childcare = models.ForeignKey(Childcare)
    content = models.TextField()
    due = models.DateTimeField(blank=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Meal(models.Model):
    content = models.TextField()
    date = models.DateField()
    childcare = models.ForeignKey(Childcare)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Event(models.Model):
    childcare = models.ForeignKey(Childcare)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=400)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)