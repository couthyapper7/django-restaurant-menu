from django.db import models
from django.contrib.auth.models import User
import os
import uuid

def category_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}.{ext}"
    return os.path.join('category', filename)

def item_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}.{ext}"
    return os.path.join('item_images', filename)


class Business(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    url_identifier = models.CharField(max_length=36, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.url_identifier:
            self.url_identifier = str(uuid.uuid4())  # Generate a unique identifier
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='categories')
    image = models.ImageField(upload_to=category_image_upload_path, null=False, blank=False, default='src/images/default/image.png')

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')
    vegan = models.BooleanField(default=False)
    sin_tacc = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
