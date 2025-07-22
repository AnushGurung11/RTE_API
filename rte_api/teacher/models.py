from django.db import models

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10)
    teacher_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.teacher_name