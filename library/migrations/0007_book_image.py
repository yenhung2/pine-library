# Generated by Django 3.0.7 on 2020-08-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_remove_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.png', height_field=100, upload_to='photos/', width_field=100),
        ),
    ]