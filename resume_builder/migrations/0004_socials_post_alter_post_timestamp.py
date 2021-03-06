# Generated by Django 4.0.1 on 2022-01-23 21:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0003_alter_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='socials',
            name='post',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='resume_builder.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 23, 16, 13, 30, 15873), null=True),
        ),
    ]
