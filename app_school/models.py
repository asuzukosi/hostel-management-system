from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
    


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


ADMIN_AUTH_LEVELS = [['super', 'super'], ['regular', 'regular'], ['minor', 'minor']]
class SchoolAdmin(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    authorization_level = models.CharField(max_length=10, choices=ADMIN_AUTH_LEVELS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=SchoolAdmin)
def post_save_receiver(sender, instance, created, **kwargs):
    """
    add user to school admin group when school admin created
    """
    if created:
        user = instance.user
        school_admin_group = Group.objects.get(name="School Admin")
        user.groups.add(school_admin_group)
        user.save()
        

@receiver(pre_delete, sender=SchoolAdmin)
def remove_school_admin_group_from_user(sender, instance, **kwargs):
    """
    remove user from school admin group when admin is deleted
    """
    user = instance.user
    school_admin_group =  Group.objects.get(name="School Admin")
    user.groups.remove(school_admin_group)
    user.save()