from django.db import models
from datetime import datetime
# Create your models here.


class Users_custom(models.Model):
    name = models.CharField(max_length=500, unique=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=32)
    DOB = models.DateField()
    phone = models.CharField(max_length=10)

    def _str_(self):
        return self.name


class Attendence(models.Model):
    user = models.ForeignKey(Users_custom, on_delete=models.CASCADE)
    Attendencein = models.DateTimeField(default=datetime.now)
    Attendenceout = models.DateTimeField(default=datetime.now)

    # def _str_(self):
    #     return str(self.Attendencein)
