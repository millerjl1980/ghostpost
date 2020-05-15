from django.db import models
from django.utils import timezone

# Create your models here.

class PostMessage(models.Model):
    boast = models.BooleanField('boast?', default=True, help_text='If it is not a boast, it will be listed as a roast!')
    content = models.CharField(max_length=280)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    sub_time = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
    hidden_key = models.CharField(max_length=6)
    
    # https://www.youtube.com/watch?v=jCzT9XFZ5bw
    @property
    def vote_score(self):
        return self.up_vote - self.down_vote

    def __str__(self):
        return self.content