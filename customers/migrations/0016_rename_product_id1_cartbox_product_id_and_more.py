# Generated by Django 5.0.1 on 2024-05-06 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0015_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartbox',
            old_name='product_id1',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='cartbox',
            old_name='user_name1',
            new_name='user_name',
        ),
    ]