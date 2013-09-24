from django.contrib.auth.models import Group
from guardian.shortcuts import assign_perm
import childcare


def roles_childcare_init_new(childcare_obj):
    # new role groups for childcare
    childcare_employees = Group.objects.get_or_create(name='%s: Employee' % childcare_obj.slug)[0]
    childcare_manager = Group.objects.get_or_create(name='%s: Manager' % childcare_obj.slug)[0]

    assign_perm('childcare_view', childcare_employees, childcare_obj)
    assign_perm('childcare_view', childcare_manager, childcare_obj)
    assign_perm('childcare_update', childcare_manager, childcare_obj)

    childcare.models.GroupChildcare.objects.get_or_create(group=childcare_employees, childcare=childcare_obj)
    childcare.models.GroupChildcare.objects.get_or_create(group=childcare_manager, childcare=childcare_obj)
    return True