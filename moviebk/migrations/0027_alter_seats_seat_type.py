# Generated by Django 4.1.6 on 2023-02-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebk', '0026_seats_seat_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seats',
            name='seat_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
