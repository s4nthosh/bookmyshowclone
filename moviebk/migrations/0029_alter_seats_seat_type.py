# Generated by Django 4.1.6 on 2023-02-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebk', '0028_alter_seats_seat_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seats',
            name='seat_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
