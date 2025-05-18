from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=10, primary_key=True)
    emp_name = models.CharField(max_length=30)
    emp_designation = models.CharField(max_length=20)
    
    def __str__(self):
        return self.emp_name