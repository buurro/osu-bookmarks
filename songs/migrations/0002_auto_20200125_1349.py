# Generated by Django 3.0.2 on 2020-01-25 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='beatmapset_id',
            new_name='beatmapset',
        ),
    ]