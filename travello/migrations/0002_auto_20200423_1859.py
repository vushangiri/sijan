# Generated by Django 3.0.4 on 2020-04-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='vid',
        ),
        migrations.AddField(
            model_name='destination',
            name='video',
            field=models.URLField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
