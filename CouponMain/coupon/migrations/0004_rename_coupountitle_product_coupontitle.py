# Generated by Django 5.0.4 on 2024-04-06 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0003_rename_coupouncode_product_couponcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='coupountitle',
            new_name='coupontitle',
        ),
    ]
