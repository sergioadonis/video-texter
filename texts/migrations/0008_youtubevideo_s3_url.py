# Generated by Django 3.0.8 on 2020-07-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0007_delete_youtubevideotask'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideo',
            name='s3_url',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
