# Generated by Django 5.1 on 2024-10-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0012_sales_invoice_sold_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_details',
            name='Address',
            field=models.TextField(max_length=50, verbose_name='Address'),
        ),
    ]
