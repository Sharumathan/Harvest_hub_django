# Generated by Django 5.0.1 on 2024-05-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0014_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
