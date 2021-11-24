from django.db import models
from django.contrib.auth.models import User
from audan.models import Building
from audan.models import Post

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    zhk = models.ForeignKey(Building, null=True, blank=True, on_delete=models.PROTECT, related_name="profile", verbose_name= ('Жилой Комплекс'))
    
    def __str__(self):
        return f'{self.user.username} Profile'

    

