# Create your models here.

from django.db import models

class Class(models.Model):
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    status_choices = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=10, choices=status_choices)
    image = models.ImageField(upload_to='student_images/',null=True,blank=True)
    selected_class = models.ForeignKey('Class', on_delete=models.CASCADE,null=True, default=True)

    def __str__(self):
        return str(self.first_name)+" "+self.last_name+" "+self.email
        #return f'{self.first_name} {self.last_name}'
