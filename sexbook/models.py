from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=300)
    

    def __str__(self):
        return str(self.name)

class Message(models.Model):
    value = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)
    user = models.CharField(max_length=300)
    room = models.CharField(max_length=1000000)
 

    def __str__(self):
        return str(self.user)
