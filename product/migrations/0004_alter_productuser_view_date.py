# Generated by Django 4.1.3 on 2022-11-25 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productuser_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productuser',
            name='view_date',
            field=models.DateTimeField(),
        ),
    ]