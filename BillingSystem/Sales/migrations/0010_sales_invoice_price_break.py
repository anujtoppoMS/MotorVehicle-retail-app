# Generated by Django 5.1 on 2024-10-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0009_alter_sales_invoice_invoice_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_invoice',
            name='Price_break',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]