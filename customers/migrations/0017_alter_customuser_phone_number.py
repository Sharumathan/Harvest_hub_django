# Generated by Django 5.0.1 on 2024-05-06 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0016_rename_product_id1_cartbox_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(unique=True),
        ),
    ]
