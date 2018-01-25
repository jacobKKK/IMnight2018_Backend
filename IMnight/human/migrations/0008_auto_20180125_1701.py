# Generated by Django 2.0.1 on 2018-01-25 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0007_auto_20180125_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='reward_list',
        ),
        migrations.AlterField(
            model_name='reward',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reward', to='human.Task'),
        ),
    ]