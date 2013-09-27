from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from utils.roles import roles_child_init_new


class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='child/images/', blank=True)
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(100, 100)],
                               format='JPEG',
                               options={'quality': 60})
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    information = models.TextField(blank=True)
    teacher_notes = models.TextField(blank=True)
    guardians = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        name = self.first_name + ' ' + self.last_name
        return name

    class Meta:
        permissions = (
            ('child_view', 'View child profile'),
            ('child_update_guardian', 'Update child - all permissions'),
            ('child_update_teacher', 'Update child - limited permissions'),
        )

    def save(self, *args, **kwargs):
        is_create = False
        if not self.id:
            is_create = True
        super(Child, self).save(*args, **kwargs)
        if is_create:
            roles_child_init_new(self)

    def get_absolute_url(self):
        return reverse('child.views.child', args=[self.pk])


class GroupChild(models.Model):
    child = models.ForeignKey(Child)
    group = models.ForeignKey(Group)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.group.name

    class Meta:
        unique_together = ['child', 'group']