# Generated by Django 3.0.7 on 2020-08-12 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20200812_0023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='summmary',
            new_name='summary',
        ),
    ]