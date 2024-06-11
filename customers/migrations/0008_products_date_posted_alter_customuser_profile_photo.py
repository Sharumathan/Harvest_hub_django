# Generated by Django 5.0.1 on 2024-04-23 06:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_customuser_joined_date_customuser_profile_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='date_posted',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_photo',
            field=models.ImageField(blank=True, default='userProfile/commonProfile.png', null=True, upload_to='userProfile'),
        ),
    ]