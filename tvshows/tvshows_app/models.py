from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 2:
            errors['title'] = "Title must be atleast 2 characters"

        if len(post_data['network']) < 3:
            errors['network'] = "Network must be atleast 2 characters"
        
        if post_data['desc'] != '' and len(post_data['desc']) < 10:
            errors['desc'] = "Description must be atleast 10 characters"
        
        if datetime.strptime(post_data['release'], '%Y-%m-%d') > datetime.now():
            errors['release'] = 'Release Date should be in the past'

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release = models.DateField()
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()