# Generated by Django 4.1.3 on 2022-11-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.TextField(null=True),
        ),
    ]