from django.contrib.auth.models import Group
from guardian.shortcuts import assign_perm
import child
import childcare


def roles_childcare_init_new(childcare_obj):
    # new role groups for childcare
    childcare_employees = Group.objects.get_or_create(name='%s: Employee' % childcare_obj.slug)[0]
    childcare_manager = Group.objects.get_or_create(name='%s: Manager' % childcare_obj.slug)[0]
    childcare_teacher = Group.objects.get_or_create(name='%s: Teacher' % childcare_obj.slug)[0]

    assign_perm('childcare_view', childcare_manager, childcare_obj)
    assign_perm('childcare_update', childcare_manager, childcare_obj)
    assign_perm('classroom_view', childcare_manager, childcare_obj)

    assign_perm('childcare_view', childcare_employees, childcare_obj)
    assign_perm('classroom_view', childcare_employees, childcare_obj)

    assign_perm('classroom_view', childcare_teacher, childcare_obj)

    childcare.models.GroupChildcare.objects.get_or_create(group=childcare_employees, childcare=childcare_obj)
    childcare.models.GroupChildcare.objects.get_or_create(group=childcare_manager, childcare=childcare_obj)
    childcare.models.GroupChildcare.objects.get_or_create(group=childcare_teacher, childcare=childcare_obj)
    return True


def roles_child_init_new(child_obj):
    # new role groups for children
    guardians = Group.objects.get_or_create(name='Child %s: Guardian' % child_obj.pk)[0]
    teachers = Group.objects.get_or_create(name='Child %s: Teacher' % child_obj.pk)[0]
    others = Group.objects.get_or_create(name='Child %s: Other' % child_obj.pk)[0]

    assign_perm('child_view', guardians, child_obj)
    assign_perm('child_update_guardian', guardians, child_obj)

    assign_perm('child_view', teachers, child_obj)
    assign_perm('child_update_teacher', teachers, child_obj)

    assign_perm('child_view', others, child_obj)

    child.models.GroupChild.objects.get_or_create(group=guardians, child=child_obj)
    child.models.GroupChild.objects.get_or_create(group=teachers, child=child_obj)
    child.models.GroupChild.objects.get_or_create(group=others, child=child_obj)
    return True