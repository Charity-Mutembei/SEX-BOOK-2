from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)
class Message(models.Model):
    message = models.CharField(max_length=1000)
    posted_on = models.DateTimeField(default=datetime.now)
    user = models.CharField(max_length=300)
    room = models.CharField(max_length=300)

    def __str__(self):
        return str(self.user)
