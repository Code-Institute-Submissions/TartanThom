# Generated by Django 3.0.5 on 2020-06-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200613_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_type',
            field=models.CharField(choices=[('cards', 'cards'), ('cake-toppers', 'cake-toppers'), ('Gifts', 'Gifts')], max_length=100),
        ),
    ]
