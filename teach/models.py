from django.db import models
# from models import Model
# Create your models here.


class DB_teach(models.Model):
    name = models.CharField(max_length=255, unique=False)
    course = models.CharField(max_length=255, unique=False)


    def __str__(self):
        return self.name, self.course