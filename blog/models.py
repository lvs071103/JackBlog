from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return '%s' %self.title

    class Meta:
        ordering = ['-timestamp']

class BackendCkeditor(models.Model):
    body = RichTextUploadingField()
