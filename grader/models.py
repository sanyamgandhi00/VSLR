
from django.db import models

# Create your models here.
class sample_answer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    college = models.TextField()
    code = models.CharField(max_length=255,null=False,blank=False)
    sample = models.FileField(upload_to='sample', blank=False, null=False)

    def __str__(self):
        return self.name


class student_answer(models.Model):
    roll = models.CharField(max_length=255)
    code = models.CharField(max_length=255,null=False,blank=False)
    answer = models.FileField(upload_to='answer', blank=False, null=False)
    score = models.CharField(max_length=255)

    def __str__(self):
        return self.roll