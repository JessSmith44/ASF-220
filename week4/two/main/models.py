from django.db import models

class Image(models.Model):
    title = models.CharField()
    image = models.ImageField(upload_to='img/%y')

    def __str__(self):
        return self.title