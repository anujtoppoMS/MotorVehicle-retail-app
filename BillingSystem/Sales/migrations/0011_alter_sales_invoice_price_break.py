# Generated by Django 5.1 on 2024-10-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0010_sales_invoice_price_break'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_invoice',
            name='Price_break',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
