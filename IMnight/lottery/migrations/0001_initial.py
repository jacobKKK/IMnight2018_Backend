# Generated by Django 2.0 on 2018-01-25 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_active_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('due_date', models.DateTimeField()),
                ('credit', models.PositiveIntegerField(default=0)),
                ('activated', models.BooleanField(default=False)),
                ('category', models.SmallIntegerField(choices=[(1, '每日任務'), (2, '限時任務'), (3, '彩蛋')], default=1)),
                ('label', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='progresstask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottery.Task'),
        ),
        migrations.AddField(
            model_name='progresstask',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
