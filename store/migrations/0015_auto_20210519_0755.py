# Generated by Django 3.1.7 on 2021-05-19 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210519_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='uploads/products/'),
        ),
    ]
