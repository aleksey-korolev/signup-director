from django.db import models

# Create your models here.
class Participants(models.Model):
    name = models.CharField(max_length=255, default='no_name')
    attendance = models.BooleanField(default=False)
    accompanyings = models.IntegerField(default=0)
    event_id = models.IntegerField()