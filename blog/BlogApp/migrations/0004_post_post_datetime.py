# Generated by Django 5.0.1 on 2024-02-06 05:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_post_post_date_alter_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]