# Generated by Django 3.0.7 on 2020-09-14 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0025_auto_20200914_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowing',
            old_name='checkout_admin',
            new_name='checkout_staff',
        ),
        migrations.RenameField(
            model_name='borrowing',
            old_name='return_admin',
            new_name='return_staff',
        ),
    ]
