from django.db import models
from django.utils import timezone
# Create your models here.


class post(models.Model):
    Title=models.CharField(max_length=100)
    contant=models.TextField(max_length=100000,blank=True , null=True)
    create_at=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='Photo')


    def __str__(self):
        return self.Title
