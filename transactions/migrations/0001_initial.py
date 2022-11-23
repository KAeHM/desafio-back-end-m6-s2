# Generated by Django 4.1.3 on 2022-11-22 14:53

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "transaction_type",
                    models.IntegerField(
                        choices=[
                            (1, "Debito"),
                            (2, "Boleto"),
                            (3, "Financiamento"),
                            (4, "Credito"),
                            (5, "Recebimento Emprestimo"),
                            (6, "Vendas"),
                            (7, "Recebimento TED"),
                            (8, "Recebimento DOC"),
                            (9, "Aluguel"),
                        ]
                    ),
                ),
                ("value", models.IntegerField()),
                (
                    "cpf",
                    models.TextField(
                        max_length=11,
                        validators=[django.core.validators.MinLengthValidator(11)],
                    ),
                ),
                (
                    "card",
                    models.TextField(
                        max_length=12,
                        validators=[django.core.validators.MinLengthValidator(12)],
                    ),
                ),
                ("transfer_date", models.DateField()),
                ("transfer_hour", models.DateField()),
                ("store_owner", models.TextField(max_length=56)),
                ("store_name", models.TextField(max_length=86)),
            ],
        ),
    ]