from django.db import models

class Exam(models.Model):
    """
    It is the model class for the Exam and 
    in the fields there are some changes to be done
    """
    
    exam_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    exam_date = models.CharField(max_length=50)
    exam_time = models.CharField(max_length=20)
    status = models. CharField(max_length=20)
    
    def __str__(self):
        return self.title
    
    