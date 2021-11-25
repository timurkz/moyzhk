from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class Building(models.Model):
    #district = models.CharField(max_length=120)
    name = models.CharField(max_length=70)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="buildings")
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name= ('Краткое описание'))
    body = models.TextField(null=True, blank=True, max_length=100, verbose_name= ('Полное описание'))
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True) 
    price = models.IntegerField(null=True, blank=True, verbose_name= ('Цена'))
    # phone_number = models.IntegerField(verbose_name= ('Номер телефона'))
    phone_number = PhoneNumberField(verbose_name= ('Номер телефона'))
    image = models.ImageField(default='default.jpg', upload_to='post_pics', verbose_name= ('Фото'))

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    zhk = models.ForeignKey(Building, on_delete=models.PROTECT, related_name="posts", verbose_name= ('Жилой Комплекс'))
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
