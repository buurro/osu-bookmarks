# Generated by Django 3.0.2 on 2020-01-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20200126_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beatmap',
            name='version',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='beatmapset',
            name='artist',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='beatmapset',
            name='creator',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='beatmapset',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
