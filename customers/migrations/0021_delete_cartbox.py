# Generated by Django 5.0.1 on 2024-05-06 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0020_remove_customuser_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartBox',
        ),
    ]