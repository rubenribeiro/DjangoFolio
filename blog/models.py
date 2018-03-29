from django.db import models
import datetime

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=1255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/blog/")
    
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
