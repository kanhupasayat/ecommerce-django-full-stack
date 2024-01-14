# Generated by Django 5.0 on 2024-01-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0005_rename_order_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='oid',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='state',
        ),
        migrations.AddField(
            model_name='orders',
            name='name2',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
    ]