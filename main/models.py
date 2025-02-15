from django.db import models
from django.contrib.auth.models import User
import os
import uuid
from PIL import Image

def business_image_upload_path(instance, filename, folder):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}-{folder}.{ext}"
    return os.path.join('business', instance.url_identifier, folder, filename)

def banner_upload_path(instance, filename):
    return business_image_upload_path(instance, filename, 'banners')

def icon_upload_path(instance, filename):
    return business_image_upload_path(instance, filename, 'icons')

class Business(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    url_identifier = models.CharField(max_length=36, unique=True, blank=True, editable=False)
    banner = models.ImageField(upload_to=banner_upload_path, null=True, blank=True)
    icon = models.ImageField(upload_to=icon_upload_path, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.url_identifier:
            self.url_identifier = str(uuid.uuid4())  # Generate a unique identifier
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Business"
        verbose_name_plural = "Businesses"

def category_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}.{ext}"
    return os.path.join('category', instance.business.name, instance.business.url_identifier, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='categories')
    image = models.ImageField(upload_to=category_image_upload_path, null=False, blank=False, default='src/static/images/default/image.png')

    def __str__(self):
        return self.name
    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"


def item_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}.{ext}"
    return os.path.join('item_images', filename)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=150, blank=True)  
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')
    vegan = models.BooleanField(default=False)
    sin_tacc = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        # First, save the model as usual
        super().save(*args, **kwargs)
        
        if self.image:
            img = Image.open(self.image.path)
            webp_image_path = os.path.splitext(self.image.path)[0] + '.webp'
            img.save(webp_image_path, 'WEBP')
            self.image.name = os.path.splitext(self.image.name)[0] + '.webp'
            super().save(*args, **kwargs)

    class Meta: 
        verbose_name = "Item"
        verbose_name_plural = "Items"