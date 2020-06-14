# Generated by Django 3.0.5 on 2020-06-14 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200614_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_type',
            field=models.CharField(choices=[('cards', 'Cards'), ('cake-toppers', 'Cake-Toppers'), ('gifts', 'Gifts')], max_length=100),
        ),
    ]
