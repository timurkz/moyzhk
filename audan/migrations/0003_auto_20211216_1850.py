# Generated by Django 3.2.9 on 2021-12-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audan', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='post_pics', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='post',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics', verbose_name='Фото'),
        ),
    ]
