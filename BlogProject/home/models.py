from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    content = models.TextField(default='No content available') 

    def __str__(self):
        return self.title
