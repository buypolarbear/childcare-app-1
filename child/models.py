from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.db import models
from utils.roles import roles_child_init_new


GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'female'),
    ('S', 'startup'),
)


class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/child/', blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    information = models.TextField(blank=True)
    #teacher_notes = models.TextField(blank=True)
    guardians = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)

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

    def get_image(self):
        try:
            return self.image
        except IOError:
            return None

    def get_absolute_url(self):
        return reverse('child.views.child', args=[self.pk])


class ChildFile(models.Model):
    file = models.FileField(upload_to='files/child/')
    description = models.CharField(max_length=500, blank=True)
    uploader = models.ForeignKey(User)
    child = models.ForeignKey(Child)
    created = models.DateTimeField(auto_now_add=True)


class TeacherNote(models.Model):
    author = models.ForeignKey(User)
    child = models.ForeignKey(Child)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class GroupChild(models.Model):
    child = models.ForeignKey(Child)
    group = models.ForeignKey(Group)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.group.name

    class Meta:
        unique_together = ['child', 'group']