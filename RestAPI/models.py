from django.db import models

class Post(models.Model):
    class Meta:
        db_table = 'Finalized_Tweets'
    tlink = models.CharField(max_length=255)
    wlink = models.CharField(max_length=255)
    user = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    spreadfactor = models.FloatField()
    hiringchance = models.FloatField()
    source = models.CharField(max_length=100)
    text = models.TextField()
    hashtags = models.JSONField()
    location = models.CharField(max_length=100, default=None)
    verified = models.BooleanField()

    def __str__(self):
        return self.tlink