from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_submitter = models.BooleanField(default=False)
    is_approver = models.BooleanField(default=False)
    is_ict= models.BooleanField(default=False)
    is_drilling = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_od = models.BooleanField(default=False)
    is_correct = models.BooleanField('correct false', default=True)

        







