# Generated by Django 5.1.2 on 2024-11-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0002_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
