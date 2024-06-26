# Generated by Django 4.2.4 on 2024-04-06 19:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('couponcode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('coupontitle', models.CharField(max_length=200)),
                ('redeemed', models.BooleanField(default=False)),
                ('saved', models.BooleanField(default=False)),
            ],
        ),
    ]
