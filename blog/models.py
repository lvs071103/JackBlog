from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return '%s' %self.title

    class Meta:
        ordering = ['-timestamp']

    
