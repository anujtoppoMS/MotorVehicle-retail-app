# Generated by Django 5.1 on 2024-10-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_remove_product_description_product_model_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='sales_status',
            field=models.BooleanField(default=False),
        ),
    ]
