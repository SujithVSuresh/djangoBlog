# Generated by Django 3.2.2 on 2021-07-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default2.png', upload_to='profile_pics'),
        ),
    ]