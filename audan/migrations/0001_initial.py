# Generated by Django 3.2.8 on 2021-11-11 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='audan.building')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='buildings', to='audan.city'),
        ),
    ]
