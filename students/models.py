from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    Name=models.CharField(max_length=120)
    RegisterNumber = models.PositiveIntegerField()
    Email= models.EmailField(unique=True)
    Grade = models.CharField(max_length=120)
    active_status = models.BooleanField(default=True)



    def __str__(self):
        return self.Name
