# Generated by Django 3.0.7 on 2020-09-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_book_date_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='status',
        ),
        migrations.AddField(
            model_name='book',
            name='borrowed',
            field=models.BooleanField(default=False),
        ),
    ]
