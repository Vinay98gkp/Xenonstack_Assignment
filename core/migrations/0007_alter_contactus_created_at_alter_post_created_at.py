# Generated by Django 4.2.2 on 2023-12-19 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_contactus_alter_post_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactus",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 19, 19, 41, 21, 993055)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 19, 19, 41, 21, 991057)
            ),
        ),
    ]
