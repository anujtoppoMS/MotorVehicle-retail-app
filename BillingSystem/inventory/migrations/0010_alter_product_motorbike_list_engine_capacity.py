# Generated by Django 5.1 on 2024-10-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_product_motorbike_list_engine_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_motorbike_list',
            name='Engine_capacity',
            field=models.PositiveIntegerField(verbose_name=int),
        ),
    ]
