# Generated by Django 2.1.8 on 2019-07-09 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editgoapp', '0004_auto_20190706_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='creator',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
