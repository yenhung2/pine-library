# Generated by Django 3.0.7 on 2020-08-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pubr', models.CharField(max_length=200)),
                ('sumy', models.TextField()),
                ('bor_date', models.DateTimeField(verbose_name='date published')),
                ('was_bor', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]