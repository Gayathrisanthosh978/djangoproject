from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    empname=models.CharField(max_length=120)
    department = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    salary = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.empname
