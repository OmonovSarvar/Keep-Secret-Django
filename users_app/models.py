from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile_images', default='profile.png')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f"{self.user.username}"
