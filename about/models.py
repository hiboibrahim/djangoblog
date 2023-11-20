from django.db import models
from Cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    author = models.CharField()


    def __str__(self):
        return self.title

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
