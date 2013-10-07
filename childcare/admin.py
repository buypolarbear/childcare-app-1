from django.contrib import admin
from childcare.models import Childcare, GroupChildcare, ChildcareNews
from website.models import WebsiteNews

admin.site.register(Childcare)
admin.site.register(GroupChildcare)
admin.site.register(ChildcareNews)