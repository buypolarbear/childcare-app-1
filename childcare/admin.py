from django.contrib import admin
from childcare.models import Childcare, GroupChildcare, ChildcareNews, Classroom

admin.site.register(Childcare)
admin.site.register(GroupChildcare)
admin.site.register(ChildcareNews)
admin.site.register(Classroom)