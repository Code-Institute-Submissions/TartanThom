# Generated by Django 3.0.5 on 2020-06-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200618_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreviews',
            name='review_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
