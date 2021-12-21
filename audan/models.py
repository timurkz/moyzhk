from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from PIL import Image, ExifTags
from io import BytesIO
from django.core.files import File
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
    User = settings.AUTH_USER_MODEL
    title = models.CharField(max_length=40, verbose_name= ('Краткое описание'))
    body = models.TextField(null=True, blank=True, max_length=300, verbose_name= ('Полное описание (Не обязательно)'))
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True) 
    price = models.IntegerField(null=True, blank=True, verbose_name= ('Цена в тенге (Не обязательно)'))
    phone_number = PhoneNumberField(verbose_name= ('Номер телефона'))
    image1 = models.ImageField(null=True, blank=True, upload_to='post_pics', verbose_name= ('Основное фото'))
    image2 = models.ImageField(null=True, blank=True, upload_to='post_pics', verbose_name=('Дополнительное фото'))
    default_image = models.ImageField(default='default.jpg')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    zhk = models.ForeignKey(Building, on_delete=models.PROTECT, related_name="posts", verbose_name= ('Жилой Комплекс'))
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image1:
            img = Image.open(BytesIO(self.image1.read()))
            if hasattr(img, '_getexif'):
                exif = img._getexif()
                if exif:
                    for tag, label in ExifTags.TAGS.items():
                        if label == 'Orientation':
                            orientation = tag
                            break
                    if orientation in exif:
                        if exif[orientation] == 3:
                            img = img.rotate(180, expand=True)
                        elif exif[orientation] == 6:
                            img = img.rotate(270, expand=True)
                        elif exif[orientation] == 8:
                            img = img.rotate(90, expand=True)

            img.thumbnail((600,600), Image.ANTIALIAS)
            output = BytesIO()
            img = img.convert('RGB')
            img.save(output, format='JPEG', quality=95)
            output.seek(0)
            self.image1 = File(output, self.image1.name)
        
        if self.image2:
            img = Image.open(BytesIO(self.image2.read()))
            if hasattr(img, '_getexif'):
                exif = img._getexif()
                if exif:
                    for tag, label in ExifTags.TAGS.items():
                        if label == 'Orientation':
                            orientation = tag
                            break
                    if orientation in exif:
                        if exif[orientation] == 3:
                            img = img.rotate(180, expand=True)
                        elif exif[orientation] == 6:
                            img = img.rotate(270, expand=True)
                        elif exif[orientation] == 8:
                            img = img.rotate(90, expand=True)

            img.thumbnail((600,600), Image.ANTIALIAS)
            output = BytesIO()
            img = img.convert('RGB')
            img.save(output, format='JPEG', quality=95)
            output.seek(0)
            self.image2 = File(output, self.image2.name)

        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
