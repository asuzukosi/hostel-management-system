from django.db import models
import uuid


HOSTEL_GENDERS = [['male', 'male'], ['female', 'female']]
# Create your models here.
class Hostel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    name = models.CharField(max_length=200)
    gender = models.CharField(choices= HOSTEL_GENDERS,max_length=200)
    capacity = models.IntegerField()
