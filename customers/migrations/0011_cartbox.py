# Generated by Django 5.0.1 on 2024-05-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_customuser_total_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
            ],
        ),
    ]
