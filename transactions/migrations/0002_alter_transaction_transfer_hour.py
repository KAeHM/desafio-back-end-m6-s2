# Generated by Django 4.1.3 on 2022-11-22 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transfer_hour",
            field=models.DateTimeField(),
        ),
    ]
