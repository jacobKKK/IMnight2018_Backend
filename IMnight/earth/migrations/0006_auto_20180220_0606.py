# Generated by Django 2.0 on 2018-02-20 06:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0005_holdingvocher_be_used'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='description',
            new_name='info',
        ),
        migrations.RemoveField(
            model_name='store',
            name='storename',
        ),
        migrations.RemoveField(
            model_name='vocher',
            name='sub_title',
        ),
        migrations.AddField(
            model_name='store',
            name='url',
            field=models.URLField(default='https://i.imgur.com/67A5cyq.jpg'),
        ),
        migrations.AddField(
            model_name='vocher',
            name='due_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='store',
            name='title',
            field=models.TextField(default='Store'),
        ),
    ]