from django.db import models

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.teacher_name