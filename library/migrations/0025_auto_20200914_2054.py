# Generated by Django 3.0.7 on 2020-09-14 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0024_auto_20200914_0131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='current_borrowing',
        ),
        migrations.RemoveField(
            model_name='book',
            name='history_borrowings',
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Book'),
        ),
    ]
