from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.db import models
from childcare import countries
from utils.roles import roles_childcare_init_new
from utils.slugify import unique_slugify


class Childcare(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    slogan = models.CharField(max_length=100)
    description = models.TextField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = countries.CountryField()
    manager = models.ForeignKey(User, related_name='childcare_manager')
    employees = models.ManyToManyField(User, related_name='childcare_employees')
    theme = models.CharField(max_length=100)
    #subscription
    #subscription_expires

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
            ('childcare_view', 'View childcare dashboard'),
            ('childcare_update', 'Update childcare settings'),
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
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.group.name

    class Meta:
        unique_together = ['childcare', 'group']