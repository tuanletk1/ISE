# Generated by Django 4.1.3 on 2022-12-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productuser_view_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_sold',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
