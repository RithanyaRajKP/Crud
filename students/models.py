from django.db import models
from django.forms import ModelForm
# Create your models here.


class Students(models.Model):

    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=15)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=10)
    occupation=models.CharField(max_length=100)


class Meta:

        db_table="students"
