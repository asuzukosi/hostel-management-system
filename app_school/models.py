from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name


ADMIN_AUTH_LEVELS = [['super', 'super'], ['regular', 'regular'], ['minor', 'minor']]
class SchoolAdmin(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    authorization_level = models.CharField(max_length=10, choices=ADMIN_AUTH_LEVELS)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()