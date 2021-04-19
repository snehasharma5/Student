from django.db import models
from django.urls import reverse


class RegisterModel(models.Model):
    enrollment_number = models.IntegerField(blank=False, primary_key=True)
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images/')

    def get_absolute_url(self):
        return reverse('student_list')

    def __str__(self):
        return self.name + " | " + str(self.enrollment_number)
