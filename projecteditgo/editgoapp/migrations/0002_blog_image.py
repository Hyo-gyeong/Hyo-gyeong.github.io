# Generated by Django 2.1.7 on 2019-07-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editgoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
