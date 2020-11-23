from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Iamge=models.ImageField(upload_to='profile/')
    Unmber_Phone=models.CharField(max_length=25,null=True,blank=True)
    Adress=models.CharField(max_length=200 ,null=True , blank=True)



    def __str__(self):
        return str(self.user)





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
