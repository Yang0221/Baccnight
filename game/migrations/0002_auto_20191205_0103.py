# Generated by Django 2.2.7 on 2019-12-05 00:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='level',
            name='body',
        ),
        migrations.AddField(
            model_name='level',
            name='image',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='time',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255)),
                ('position_x', models.IntegerField()),
                ('position_y', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('id_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Level')),
            ],
        ),
    ]