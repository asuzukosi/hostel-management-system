from django.db import models

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

        