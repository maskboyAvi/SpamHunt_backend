# Generated by Django 5.0 on 2023-12-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sms", "0003_remove_sms_sms_sms_label"),
    ]

    operations = [
        migrations.AddField(
            model_name="sms",
            name="sms",
            field=models.CharField(default="Null", max_length=10000),
        ),
    ]
