# Generated by Django 2.2.8 on 2020-01-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_level_world'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='detail1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='detail2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='detail3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='detail4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='detail5',
            field=models.BooleanField(default=False),
        ),
    ]
