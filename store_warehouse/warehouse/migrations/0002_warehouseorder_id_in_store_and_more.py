# Generated by Django 4.2.3 on 2023-07-22 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouseorder',
            name='id_in_store',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='warehouseorder',
            name='order_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
