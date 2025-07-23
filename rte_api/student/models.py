from django.db import models

class Student(models.Model):
    lmu_id = models.IntegerField( unique=True)
    student_name = models.CharField(max_length=100)
    year = models.IntegerField(default=1)
    intake = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    course = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.student_name