from django.db import models
from django.utils import timezone

# Create your models here.

class PostMessage(models.Model):
    boast = models.BooleanField('boast?', default=True, help_text='If it is not a boast, it will be listed as a roast!')
    content = models.CharField(max_length=280)
    up_vote = models.IntegerField()
    down_vote = models.IntegerField()
    sub_time = models.DateTimeField(default=timezone.now)