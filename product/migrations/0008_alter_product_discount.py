# Generated by Django 4.1.3 on 2022-12-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]