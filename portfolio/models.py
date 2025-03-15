from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField()

    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    number = models.CharField(max_length=13)
    Message = models.TextField(max_length=200)