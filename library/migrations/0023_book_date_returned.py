# Generated by Django 3.0.7 on 2020-09-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0022_auto_20200911_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_returned',
            field=models.DateTimeField(null=True, verbose_name='date returned'),
        ),
    ]
