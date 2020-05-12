from django.db import models
# to import module of user 
from django.contrib.auth.models import User
# to import library for slug 
from django.utils.text import slugify

# to import datatime of python
import datetime


# Create your models here.

class Note(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE) 
    title   = models.CharField(max_length=50)
    slug    = models.SlugField(null=True, blank=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)
    active  = models.BooleanField(default=True)
    tags    = models.CharField(max_length=50, blank=True)


    # to overwrite on save method to automatic save slug 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Note, self).save(*args, **kwargs)

    # to show title for each row
    def __str__ (self):
        return self.title