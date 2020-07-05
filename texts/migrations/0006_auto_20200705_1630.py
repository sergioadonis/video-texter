# Generated by Django 3.0.8 on 2020-07-05 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0005_auto_20200705_0331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtubevideo',
            name='task_id',
        ),
        migrations.CreateModel(
            name='YoutubeVideoTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(blank=True, default='', max_length=255)),
                ('youtubevideo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='texts.YoutubeVideo')),
            ],
        ),
    ]
