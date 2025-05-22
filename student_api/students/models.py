from django.db import models

# Create your models here.


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    course = models.CharField()
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=255)
    parent_contact_number = models.CharField(max_length=10)
    is_deleted = models.BooleanField(default=False)  
    def __str__(self):
        return self.full_name
