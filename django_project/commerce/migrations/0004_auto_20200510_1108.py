# Generated by Django 3.0.6 on 2020-05-10 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='nom',
            new_name='name',
        ),
    ]