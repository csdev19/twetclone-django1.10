from django.db import models

# Create your models here.

class Tweet(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}. {}".format(self.id, self.content[:20])
