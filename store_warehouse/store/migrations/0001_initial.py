# Generated by Django 4.2.3 on 2023-07-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('new', 'New'), ('in progress', 'In progress'), ('stored', 'Stored'), ('send', 'Send')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
