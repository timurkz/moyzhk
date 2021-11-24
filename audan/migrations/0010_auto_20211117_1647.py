# Generated by Django 3.2.8 on 2021-11-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audan', '0009_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
