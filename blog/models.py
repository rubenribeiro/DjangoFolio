from django.db import models
import datetime

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=1255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/blog/")

    def __str__(self):
        return self.title
