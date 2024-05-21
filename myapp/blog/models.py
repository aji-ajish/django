from django.db import models
from django.utils.text import slugify


class Categories(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) :
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,null=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) :
        return self.title


class AboutUs(models.Model):
    content=models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    picture=models.ImageField(null=True,upload_to='images/')

    def __str__(self) :
        return self.name

