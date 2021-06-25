import os
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from PIL import Image
    


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="app_school/school/",blank=True, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

@receiver(post_save, sender=School)
def resize_logo(sender, instance, **kwargs):
    # resize school logo to standard 100 x 100 size once school instance has been saved
    if instance.logo != None:
        image = Image.open(instance.logo)
        image.thumbnail((100, 100))
        image.save(os.path.join("media", instance.logo.name))





ADMIN_AUTH_LEVELS = [['super', 'super'], ['regular', 'regular'], ['minor', 'minor']]
class SchoolAdmin(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="app_school/school_admin/", blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    authorization_level = models.CharField(max_length=10, choices=ADMIN_AUTH_LEVELS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} of school {self.school}'

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

@receiver(post_save, sender=SchoolAdmin)
def resize_profile_image(sender, instance, **kwargs):
    # Resize profile image to 200 x 200 standard size once school admin has been saved
    if instance.profile_image:
        image = Image.open(instance.profile_image)
        image.thumbnail((200, 200))
        image.save(os.path.join("media", instance.profile_image.name))