from datetime import date, timedelta
from django.db import models

# Create your models here.
class Mission(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    

    def __str__(self):
        return self.title
