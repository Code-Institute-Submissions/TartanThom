# Generated by Django 3.0.5 on 2020-06-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='test', editable=False, max_length=32),
            preserve_default=False,
        ),
    ]
